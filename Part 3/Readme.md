# Part 3: Practical Audit – AI Ethics Project

## 🎯 Task Overview

- **Dataset:** COMPAS Recidivism Dataset  
- **Toolkit:** IBM’s AI Fairness 360 (AIF360)  
- **Goal:** Audit for racial bias in risk scores  
- **Deliverable:** Python code + visualizations + report

---

## 🧪 Methodology

This audit used the COMPAS dataset to analyze potential racial bias in predicting recidivism. We focused on the disparity in **false positive rates (FPR)** — that is, how often people were wrongly predicted to reoffend.

Steps:
1. Loaded the dataset using AIF360
2. Defined `race` as the sensitive attribute
3. Applied the **Reweighing** bias mitigation technique
4. Trained a logistic regression model
5. Compared FPR between:
   - **Privileged group**: Caucasian
   - **Unprivileged group**: African-American
6. Visualized the disparity in a bar chart

---

## 📊 Results

### False Positive Rates (FPR):
- **Privileged group (Caucasian):** `0.6221`
- **Unprivileged group (African-American):** `0.3445`
- **Disparity (Unprivileged – Privileged):** `-0.2776`

This result shows an **inverse disparity**, meaning Caucasians were more likely to be falsely labeled as high-risk than African-Americans. While this may appear favorable for the unprivileged group, it still represents an imbalance that requires attention.

---

## ✅ Remediation Strategy

We used the **Reweighing** algorithm to adjust instance weights during training. While it improved balance, it did not eliminate bias — and in this case, inverted the disparity.

### Suggested further steps:
- **Adversarial Debiasing** (in-processing)
- **Equalized Odds Post-processing**
- Improve training data diversity and representativeness

---

## 🧠 Conclusion

This audit highlights that even fairness interventions can produce new forms of bias if not carefully tuned. Regular audits using tools like AIF360 are essential for building ethical AI — especially in domains like criminal justice where decisions deeply impact lives.

> ⚖️ Fair AI isn’t just technical — it’s social responsibility in action.
