import pandas as pd
import matplotlib.pyplot as plt
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import numpy as np
import seaborn as sns

# Load dataset
dataset = CompasDataset()

# Define privileged and unprivileged groups
privileged_groups = [{'race': 1}]  # Caucasian
unprivileged_groups = [{'race': 0}]  # African-American

# Split into train/test
dataset_train, dataset_test = dataset.split([0.7], shuffle=True)

# Reweighing to mitigate bias
RW = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_train_transf = RW.fit_transform(dataset_train)

# Train logistic regression
scaler = StandardScaler()
X_train = scaler.fit_transform(dataset_train.features)
y_train = dataset_train.labels.ravel()

model = LogisticRegression()
model.fit(X_train, y_train)

# Test data
X_test = scaler.transform(dataset_test.features)
y_pred = model.predict(X_test)

# Add predictions
dataset_pred = dataset_test.copy()
dataset_pred.labels = y_pred.reshape(-1,1)

# Metrics
classified_metric = ClassificationMetric(dataset_test, dataset_pred,
                                         unprivileged_groups=unprivileged_groups,
                                         privileged_groups=privileged_groups)

# Visualize false positive rate disparity
fpr_priv = classified_metric.false_positive_rate(privileged=True)
fpr_unpriv = classified_metric.false_positive_rate(privileged=False)
disparity = fpr_unpriv - fpr_priv

# Visualize the disparity in false positive rates
plt.bar(['Privileged', 'Unprivileged'], [fpr_priv, fpr_unpriv], color=['green', 'red'])
plt.title(f'False Positive Rate Disparity\nDifference: {disparity:.2f}')
plt.ylabel('False Positive Rate')

# Show the plot first
plt.show()

# Then print the FPR values
print("\n--- False Positive Rates ---")
print(f"Privileged group (Caucasian) FPR: {fpr_priv:.4f}")
print(f"Unprivileged group (African-American) FPR: {fpr_unpriv:.4f}")
print(f"Disparity (Unprivileged - Privileged): {disparity:.4f}")
