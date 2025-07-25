from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    Gender = request.form.get('Gender')
    Married = request.form.get('Married')
    Dependents = request.form.get('Dependents')
    Education = request.form.get('Education')
    Self_Employed = request.form.get('Self_Employed')
    ApplicantIncome = request.form.get('ApplicantIncome')
    LoanAmount = request.form.get('LoanAmount')
    Credit_History = request.form.get('Credit_History')
    Property_Area = request.form.get('Property_Area')

    prediction = utils.preprocessdata(
        Gender, Married, Dependents, Education, Self_Employed,
        ApplicantIncome, LoanAmount, Credit_History, Property_Area
    )

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__': 
    app.run(debug=True) 