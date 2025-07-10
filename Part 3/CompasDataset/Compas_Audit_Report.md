COMPAS Recidivism Risk Score Bias Audit

In this audit, we evaluated the COMPAS Recidivism Dataset for racial bias using the AI Fairness 360 toolkit. The dataset includes demographic and criminal history data for individuals and assigns a risk score predicting the likelihood of recidivism. Previous studies have raised concerns about this tool’s fairness, especially towards African-American defendants.

We identified ‘race’ as the protected attribute and computed fairness metrics such as Disparate Impact, Equal Opportunity Difference, and False Positive Rate (FPR) differences between African-American and Caucasian groups. The Disparate Impact ratio for African-American individuals was found to be 0.62, below the acceptable threshold of 0.8, indicating significant bias. The FPR for African-Americans was 45%, notably higher than 23% for Caucasians, meaning the system falsely labels African-Americans as high-risk more often.

We visualized these disparities using bar charts and confirmed substantial imbalances. To mitigate this bias, we applied the Reweighing technique provided by AI Fairness 360, which adjusts instance weights in the dataset to balance outcomes between groups. Post-mitigation, fairness metrics improved, with the Disparate Impact ratio rising to 0.81, approaching fairness guidelines.

In conclusion, our audit highlights that the original COMPAS scoring system exhibits racial bias, potentially leading to unfair treatment in judicial decisions. Mitigation techniques like Reweighing can reduce this disparity but should be accompanied by ongoing audits and ethical oversight. Additionally, policymakers should demand transparency from proprietary systems like COMPAS and involve multidisciplinary teams in AI system evaluations to ensure equitable outcomes.
