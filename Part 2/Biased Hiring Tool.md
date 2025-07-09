**Scenario:** Amazon’s AI Recruiting Tool Penalized Female Candidates
Amazon developed an AI-based recruitment tool that reportedly downgraded resumes with the word “women” (e.g., “women’s chess club captain”) and favored male-coded resumes. This is a classic example of algorithmic bias in hiring.

** 1. Source of Bias**
 Training Data Bias
The AI was trained on historical hiring data from Amazon, which was largely male-dominated — especially in technical roles. The model learned to replicate those past patterns and penalized resumes that didn’t match that profile (e.g., female applicants or gendered terms).

Other potential sources:

Lack of feature oversight: Gendered keywords were not filtered out.

Model interpreted correlations as causation: It assumed male-associated features equated to hiring success.


** 2. Proposed Fixes**
 a) Rebalance the Training Data
Use a gender-balanced dataset or apply re-weighting techniques to ensure that the model doesn’t associate success with gendered patterns.

** b) Remove Gender-Sensitive Features**
Filter out or anonymize features that can leak gender signals (e.g., names, clubs, pronouns, associations). Use NLP techniques to de-bias the input features.

** c) Include Human Oversight in the Loop**
Have diverse human reviewers periodically audit AI decisions and approve final shortlists. Use AI as a screening aid — not the sole decision-maker.


** 3. Fairness Evaluation Metrics**
After corrections, assess fairness using these metrics:

** a) Demographic Parity**
Check if selection rates are similar across gender groups:

P(select | female) ≈ P(select | male)

** b) Equal Opportunity (True Positive Rate Parity)**
Ensure qualified female and male candidates have equal chances of being selected:

TPR_female ≈ TPR_male

** c) Bias Impact Ratio (4/5ths Rule)**
Selection rate of the protected group (e.g., women) should be at least 80% of the majority group’s selection rate.

