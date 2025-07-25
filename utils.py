import numpy as np
import joblib

def preprocessdata(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, LoanAmount, Credit_History, Property_Area):
    gender_map = {"Male": 1, "Female": 0}
    married_map = {"Yes": 1, "No": 0}
    education_map = {"Graduate": 1, "Not Graduate": 0}
    self_employed_map = {"Yes": 1, "No": 0}
    property_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}

    if Dependents == '3+':
        Dependents = 3
    else:
        try:
            Dependents = int(Dependents)
        except ValueError:
            Dependents = 0  

    # Apply same log transformation as during training
    Applicant_income_log = np.log(float(ApplicantIncome) + 1)
    LoanAmount_log = np.log(float(LoanAmount) + 1)

    test_data = [[
        gender_map.get(Gender, 0),
        married_map.get(Married, 0),
        Dependents,
        education_map.get(Education, 0),
        self_employed_map.get(Self_Employed, 0),
        float(Credit_History),
        property_map.get(Property_Area, 0),
        Applicant_income_log,
        LoanAmount_log
    ]]

    trained_model = joblib.load("model.pkl")
    prediction = trained_model.predict(test_data)
    return prediction
