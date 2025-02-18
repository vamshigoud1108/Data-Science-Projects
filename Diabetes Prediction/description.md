# Diabetes Prediction
![](https://www.cdc.gov/diabetes/news/media/images/Diabetesaboutpage.jpg)

## Project Overview
The main objective of the Diabetes Prediction project is to analyze various health-related features of patients, such as glucose levels, blood pressure, insulin levels, and more, to predict whether a patient has diabetes or not. Early prediction of diabetes can help in taking preventive measures and improving patient outcomes.

## About the Dataset
The dataset used in this project comprises multiple health indicators and a target variable indicating whether a patient has diabetes. The goal is to build machine learning models to classify diabetic and non-diabetic individuals accurately.

## Data Dictionary
|Column Name | Description |
| --- | --- |
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg)|
| SkinThickness | Skin fold thickness (mm)|
| Insulin |2-Hour serum insulin (mu U/ml)| 
| BMI | Body mass index (weight in kg / height in m^2)|
| DiabetesPedigreeFunction | Diabetes pedigree function|
| Age | Age (years) |
| Outcome | Class variable (0: No diabetes, 1: Diabetes)|

## Conclusion
From the Exploratory Data Analysis (EDA), the key features influencing diabetes prediction include:
- **Glucose levels**: Higher glucose levels are more likely to be associated with diabetes.
- **BMI**: Higher BMI increases the likelihood of diabetes.
- **Insulin levels**: Abnormal insulin levels show a pattern linked to diabetes.

In terms of machine learning models, I implemented various classification algorithms — Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes (BernoulliNB), and Support Vector Machine (SVM).Among these SVM model demonstrated the best performance with an accuracy of 74%, effectively classifying diabetic and non-diabetic individuals.



