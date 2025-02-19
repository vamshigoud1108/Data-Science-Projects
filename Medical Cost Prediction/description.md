# Medical Cost Prediction
![](https://miro.medium.com/v2/resize:fit:1400/0*ssbGU5VIxtVB6NrF)
## Project Overview
This data science project aims to predict individual medical costs using a dataset containing various attributes related to health insurance. The project focuses on analyzing features such as age, gender, BMI, number of children, smoking status, region, and predicting the corresponding medical costs.
## Data Dictionary
The dataset used in this project provides information about health insurance beneficiaries and their medical costs. It includes the following columns:

| Variable | Description |
| --- | --- |
| age | age of primary beneficiary |
|bmi | body mass index |
|children | number of children covered by health insurance |
|smoker | smoking |
|region | the beneficiary's residential area in the US |
|charges | individual medical costs billed by health insurance |
## Objective
The primary objective of this project is to develop a predictive model that can accurately forecast individual medical costs based on their attributes.
## Impact
This project demonstrates how machine learning can accurately predict medical expenses based on patient data. By identifying key factors like BMI, smoking status, and age, it provides insights that can help insurance companies, healthcare providers  estimate costs, improve planning, and support better financial decision-making for patients.
## Conclusion
From the Exploratory Data Analysis (EDA), it was observed that key factors influencing medical expenses include:
- **Smoking Habits**: Smokers incur significantly higher medical expenses compared to non-smokers.
- **BMI**: Patients with a BMI greater than 30 (obese) have higher medical expenses than those with a BMI below 30.
- **Age**: Older patients tend to have higher medical expenses compared to younger patients.
Thus, medical expenses are strongly influenced by factors such as age, BMI, and smoking habits.

Coming to the evaluation of the machine learning models, I employed regression models, including Linear Regression, K-Nearest Neighbors (KNN), Decision Tree Regressor, and Random Forest Regressor. Among these, the Random Forest Regressor outperformed the others, achieving a high R² score of 87% and the lowest RMSE value. Therefore, it is the most effective model for accurately predicting medical expenses.

