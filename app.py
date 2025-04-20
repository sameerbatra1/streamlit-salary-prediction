import streamlit as st
import pickle as pkl

with open('xgb_classifier_selected_down.pkl', 'rb') as f:
    model = pkl.load(f)

st.title("Salary Prediction App")

roles = [
    "AI Engineer",
    "Analytics Engineer",
    "Applied Scientist",
    "BI Developer",
    "Business Intelligence Analyst",
    "Business Intelligence Developer",
    "Business Intelligence Engineer",
    "Data Analyst",
    "Data Analytics Manager",
    "Data Architect",
    "Data Engineer",
    "Data Manager",
    "Data Science",
    "Data Science Consultant",
    "Data Science Manager",
    "Data Scientist",
    "Data Specialist",
    "ML Engineer",
    "Machine Learning Engineer",
    "Machine Learning Infrastructure Engineer",
    "Machine Learning Scientist",
    "Other",
    "Research Analyst",
    "Research Engineer",
    "Research Scientist"
]

selected_role = st.selectbox("Select your role:", roles)

experience_level = [
    'Entry-level',
    'Executive-level',
    'Mid-level',
    'Senior-level',
]

selected_experience_level = st.selectbox("Select your experience level:", experience_level)

employement_type = [
    'Contract',
    'Full-time',
    'Part-time'
]

selected_employement_type = st.selectbox("Select your employment type:", employement_type)

role_mapping = {role: index for index, role in enumerate(roles)}
mapped_role = role_mapping[selected_role]

experience_mapping = {level: index for index, level in enumerate(experience_level)}
mapped_experience = experience_mapping[selected_experience_level]

employment_mapping = {etype: index for index, etype in enumerate(employement_type)}
mapped_employment = employment_mapping[selected_employement_type]

input_data = [[mapped_experience, mapped_role, mapped_employment]]

income_category_mapping = {
    'High income ($100,000+)': 0,
    'Low income (<$30,000)': 1,
    'Lower-middle income ($30,000 to $49,999)': 2,
    'Middle income $50,000 to $74,999': 3,
    "Upper middle income - $75000 to $99,999": 4
}

if st.button("Predict Salary"):
    predicted_salary = model.predict(input_data)
    for category, value in income_category_mapping.items():
        if value == predicted_salary[0]:
            st.write(f"Predicted salary range: {category}")
            break

    # # Additional information from the model
    # if hasattr(model, "predict_proba"):
    #     salary_probabilities = model.predict_proba(input_data)
    #     st.write("Prediction probabilities for each salary range:")
    #     st.write(salary_probabilities)

    # if hasattr(model, "feature_importances_"):
    #     st.write("Feature importances (if available):")
    #     st.write(model.feature_importances_)