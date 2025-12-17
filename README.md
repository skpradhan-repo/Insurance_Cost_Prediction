🏥 Insurance Cost Prediction Using Machine Learning



An end-to-end machine learning project to predict personalized health insurance premiums using demographic and health-related data. This project covers data visualization, statistical analysis, machine learning modeling, and deployment.

---

📌 Project Overview


Health insurance pricing is traditionally based on actuarial tables and historical averages, which often fail to capture individual-level risk accurately. This project leverages machine learning and analytics to predict insurance premiums more precisely using personal health profiles.

The solution demonstrates a complete data science lifecycle, making it ideal for portfolio and real-world use cases.

---

🎯 Objectives


Predict health insurance premiums accurately

Identify key risk factors influencing insurance cost

Provide data-driven insights for insurers

Deploy a real-time premium prediction web application

---

🧠 Business Value

Precision Pricing: Fair premiums aligned with individual risk

Risk Assessment: Identification of high-impact health factors

Customer Satisfaction: Transparent and explainable pricing

Strategic Insights: Support for policy design and market decisions

---

📊 Dataset Description

The dataset contains 11 features describing demographic and health conditions:


| Feature                 | Description                       |

| ----------------------- | --------------------------------- |

| Age                     | 18–66 years                       |

| Diabetes                | Binary (0/1)                      |

| BloodPressureProblems   | Binary (0/1)                      |

| AnyTransplants          | Binary (0/1)                      |

| AnyChronicDiseases      | Binary (0/1)                      |

| Height                  | 145–188 cm                        |

| Weight                  | 51–132 kg                         |

| KnownAllergies          | Binary (0/1)                      |

| HistoryOfCancerInFamily | Binary (0/1)                      |

| NumberOfMajorSurgeries  | 0–3                               |

| PremiumPrice            | Target variable (₹15,000–₹40,000) |



---


🛠️ Tech Stack


Programming: Python

Data Analysis: Pandas, NumPy

Visualization: Tableau, Matplotlib, Seaborn

Statistics: SciPy, Statsmodels

Machine Learning: Scikit-learn

Model Explainability: SHAP

Deployment: Flask / Streamlit

Version Control: Git \& GitHub

---



📈 Project Workflow

```

Data Collection

     ↓

Data Visualization (Tableau)

     ↓

EDA \& Hypothesis Testing

     ↓

Feature Engineering

     ↓

Machine Learning Modeling

     ↓

Model Evaluation \& Explainability

     ↓

Web App Deployment



📊 Block 1: Tableau Visualization

Dashboards Created

Summary Statistics Dashboard

 Average premium, age, and health condition distributions

Premium Pricing Analysis

 Premium distribution, age-based trends, correlation heatmaps

Risk Factors Analysis

 Impact of surgeries, chronic diseases, transplants

Demographic Insights

 BMI vs premium analysis

Key Features


Interactive filters

Drill-down capabilities

Informative tooltips

---



🔍 Block 2: Exploratory Data Analysis \& Hypothesis Testing


Exploratory Data Analysis

Distribution plots for numerical variables

Correlation heatmaps

Outlier detection using IQR and Z-score


Hypothesis Testing

T-tests / ANOVA

 Effect of chronic diseases and surgeries on premiums

Chi-Square Tests

 Association between categorical variables

Regression Analysis

 Quantifying feature impact on insurance cost

---



🤖 Block 3: Machine Learning Modeling


Data Preprocessing

Missing value checks

Feature engineering (BMI from height \& weight)

Scaling numerical features

Encoding categorical features


Models Implemented

Linear Regression (Baseline)

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Models


Model Evaluation


K-fold cross-validation

Metrics used:

 RMSE

 MAE

 R² Score


Model Interpretability



Feature importance analysis

SHAP value explanations

Business-driven insights



---



🌐 Block 4: Web-Based Insurance Premium Calculator


The final model is deployed as a real-time web application.


Deployment Options


Flask API

 REST endpoint accepting JSON input

 Returns predicted insurance premium


Streamlit Application:

 User-friendly interface

 Real-time premium estimation


Deployment Objectives:

Accessibility for non-technical users

Real-world usability

Recruiter-ready demonstration

---


📌 Key Insights


Chronic diseases and major surgeries significantly increase premiums

Age and BMI are strong numerical predictors

Tree-based models outperform linear regression

Explainable ML improves trust and transparency

---

🚀 Future Enhancements

Include lifestyle factors (smoking, exercise)

Add geographical risk features

Dockerize the application

Deploy to cloud platforms (AWS / GCP)

Implement model monitoring and retraining


---

▶️ How to Run the Project


Clone the Repository

```bash

git clone https://github.com/your-username/insurance-cost-prediction.git

cd insurance-cost-prediction

```

Install Dependencies

```bash

pip install -r requirements.txt

```

Run Streamlit App



```bash

streamlit run app.py

```

Run Flask API



```bash

python app.py

```

📎 Project Structure (Suggested)

```

insurance-cost-prediction/

│

├── data/

│   └── insurance.csv

│

├── notebooks/

│   ├── EDA\_and\_Hypothesis\_Testing.ipynb

│   └── ML\_Modeling.ipynb

│

├── reports/

│   ├── EDA\_and\_Hypothesis\_Testing.pdf

│   ├── ML\_Modeling\_Insurance\_Cost\_Prediction.pdf

│

├── models/

│   ├── linear\_regression\_model.pkl

│   ├── decision\_tree\_model.pkl

│   ├── random\_forest\_insurance\_model.pkl

│   └── xgboost\_model.pkl

│

├── tableau/

│   ├── dashboards/

│   │   ├── Summary\_Statistics.twb

│   │   ├── Premium\_Pricing\_Analysis.twb

│   │   ├── Risk\_Factors\_Analysis.twb

│   │   └── Demographic\_Insights.twb

│   │

│   ├── screenshots/

│   │   ├── Summary\_Statistics.png

│   │   ├── Premium\_Pricing\_Analysis.png

│   │   ├── Risk\_Factors\_Analysis.png

│   │   └── Demographic\_Insights.png

│   │

│   └── tableau\_public\_link.txt

│

├── web\_app/

│   ├── app.py

│   ├── api.py

│   ├── assets/

│   ├── models/

│   │   ├── linear\_regression\_model.pkl

│   │   ├── decision\_tree\_model.pkl

│   │   ├── random\_forest\_insurance\_model.pkl

│   │   └── xgboost\_model.pkl

│   │

│   ├── sample\_result.png

│   └── web\_calculator\_demo.mp4

│

├── requirements.txt

└── README.md



---
<img width="1134" height="1959" alt="image" src="https://github.com/user-attachments/assets/b0fff7ad-1c7c-4840-aae4-13928530925f" />




👤 Author



Samaresh Kumar Pradhan

📧 Email: samarescv@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/samaresh-pradhan-jee/

🔗 Medium: https://medium.com/@samarescv

---



⭐ If you found this project useful, feel free to star the repository!



---



