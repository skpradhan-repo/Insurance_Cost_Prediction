import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration & Branding
# -----------------------------
st.set_page_config(
    page_title="Insurance Premium Calculator",
    page_icon="💰",
    layout="wide"
)

# Logo or Banner
st.image("assets/insurance_logo.png", width=200)  # replace with your logo
st.markdown("<h1 style='text-align:center; color:darkblue;'>Insurance Premium Calculator</h1>", unsafe_allow_html=True)
st.markdown("---")
st.info("💡 Enter your personal and health details and click 'Predict Premium' to see estimated insurance costs.")

# -----------------------------
# Load Models
# -----------------------------
loaded_rf_model = joblib.load('random_forest_insurance_model.pkl')
loaded_dt_model = joblib.load('decision_tree_model.pkl')
loaded_xgb_model = joblib.load('xgboost_model.pkl')
loaded_lr_model = joblib.load('linear_regression_model.pkl')

models = {
    "Random Forest": loaded_rf_model,
    "Decision Tree": loaded_dt_model,
    "XGBoost": loaded_xgb_model,
    "Linear Regression": loaded_lr_model
}

# -----------------------------
# Helper function for binary radio buttons
# -----------------------------
def radio_to_binary(label, default="No"):
    choice = st.radio(label, ["Yes", "No"], index=0 if default=="Yes" else 1)
    return 1 if choice=="Yes" else 0

# -----------------------------
# Input Section (Expanders)
# -----------------------------
with st.expander("Personal Details"):
    Age = st.number_input("Age", min_value=18, max_value=100, value=35, help="Your age in years")
    Height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    Weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=75)
    Obese = radio_to_binary("Obese", default="No")

with st.expander("Health Conditions"):
    Diabetes = radio_to_binary("Diabetes", default="No")
    BloodPressureProblems = radio_to_binary("Blood Pressure Problems", default="Yes")
    AnyTransplants = radio_to_binary("Any Transplants", default="No")
    AnyChronicDiseases = radio_to_binary("Any Chronic Diseases", default="Yes")
    KnownAllergies = radio_to_binary("Known Allergies", default="No")
    HistoryOfCancerInFamily = radio_to_binary("History of Cancer in Family", default="No")
    NumberOfMajorSurgeries = st.number_input("Number of Major Surgeries", min_value=0, max_value=20, value=1)

with st.expander("Risk Scores & Interactions"):
    Height_m = st.number_input("Height in meters", min_value=0.5, max_value=2.5, value=1.7)
    BMI = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.95)
    ChronicConditionCount = st.number_input("Chronic Condition Count", min_value=0, max_value=10, value=2)
    AgeGroup_31_45 = st.checkbox("Age Group 31-45", value=True)
    AgeGroup_46_66 = st.checkbox("Age Group 46-66", value=False)
    Weight_Height_Ratio = st.number_input("Weight/Height Ratio", value=0.441)
    Age_ChronicInteraction = st.number_input("Age x Chronic Interaction", value=70)
    Surgery_ChronicInteraction = st.number_input("Surgery x Chronic Interaction", value=2)
    HealthRiskScore = st.number_input("Health Risk Score", min_value=0, max_value=10, value=3)
    AgeQuantile = st.number_input("Age Quantile", min_value=0, max_value=5, value=1)
    FamilyHealthRisk = st.number_input("Family Health Risk", min_value=0, max_value=5, value=1)
    SurgeryBurden_Low = st.checkbox("Surgery Burden Low", value=False)
    SurgeryBurden_High = st.checkbox("Surgery Burden High", value=True)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Premium"):
    # Collect input data into DataFrame
    input_data = {
        "Age": Age,
        "Diabetes": Diabetes,
        "BloodPressureProblems": BloodPressureProblems,
        "AnyTransplants": AnyTransplants,
        "AnyChronicDiseases": AnyChronicDiseases,
        "Height": Height,
        "Weight": Weight,
        "KnownAllergies": KnownAllergies,
        "HistoryOfCancerInFamily": HistoryOfCancerInFamily,
        "NumberOfMajorSurgeries": NumberOfMajorSurgeries,
        "Height_m": Height_m,
        "BMI": BMI,
        "ChronicConditionCount": ChronicConditionCount,
        "AgeGroup_31-45": AgeGroup_31_45,
        "AgeGroup_46-66": AgeGroup_46_66,
        "Weight_Height_Ratio": Weight_Height_Ratio,
        "Age_ChronicInteraction": Age_ChronicInteraction,
        "Surgery_ChronicInteraction": Surgery_ChronicInteraction,
        "HealthRiskScore": HealthRiskScore,
        "AgeQuantile": AgeQuantile,
        "FamilyHealthRisk": FamilyHealthRisk,
        "Obese": Obese,
        "SurgeryBurden_Low": SurgeryBurden_Low,
        "SurgeryBurden_High": SurgeryBurden_High
    }

    X_input = pd.DataFrame([input_data])

    # -----------------------------
    # Predictions
    # -----------------------------
    results = []
    for name, model in models.items():
        pred = model.predict(X_input)[0]
        results.append({"Model": name, "Predicted Premium": round(pred, 2)})

    results_df = pd.DataFrame(results)

    # Display results table with highlights
    st.subheader("Prediction Results:")
    st.dataframe(
        results_df.style
        .highlight_max(axis=0, color='lightgreen')
        .highlight_min(axis=0, color='lightcoral')
    )

    # Display bar chart for visual comparison
    st.subheader("Visual Comparison")
    st.bar_chart(results_df.set_index('Model'))