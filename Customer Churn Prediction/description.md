# Customer Churn Prediction
![](https://miro.medium.com/v2/resize:fit:1400/1*47xx1oXuebvYwZeB0OutuA.png)
## Project Overview
The main objective of the Customer Churn Prediction project is to analyze the demographics, service details, and financial metrics of telecom customers, including factors like gender, senior citizen status, tenure, contract type, monthly charges, and more, to predict whether a customer will leave the telecom service or not. Customer churn, the decision of customers to leave a telecom service, can significantly impact the company's revenue and growth. By accurately predicting customer churn, the telecom company can take proactive measures to retain valuable customers and improve overall customer satisfaction.
## About the Dataset
The dataset used in this project is sourced from ![Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and comprises 7,043 rows and 21 columns. The primary objective of the dataset is to predict whether a telecom customer will churn (leave the service) based on their demographics, service details, and financial information.

## Data Dictionary
| Column Name | Description |
| --- | --- |
| CustomerId | Unique identification key for each customer |
| Gender | Gender of the customer (Male/Female)|
| SeniorCitizen | Binary flag indicating if the customer is a senior citizen (1 = Yes, 0 = No) |
|Partner | Binary flag indicating if the customer has a partner (1 = Yes, 0 = No) |
|Dependents | Binary flag indicating if the customer has dependents (1 = Yes, 0 = No) |
|Tenure | Number of months the customer has been with the telecom service |
|PhoneService | Binary flag indicating if the customer has phone service (1 = Yes, 0 = No) |
|MultipleLines | Binary flag indicating if the customer has multiple lines (1 = Yes, 0 = No) |
|InternetService | Type of internet service subscribed to by the customer (DSL, Fiber optic, or None) |
|OnlineSecurity | Binary flag indicating if the customer has online security add-on (1 = Yes, 0 = No) |
|TechSupport | Binary flag indicating if the customer has tech support add-on (1 = Yes, 0 = No) |
|Contract | Type of contract (Month-to-month, One year, or Two year) |
|MonthlyCharges | Monthly charges paid by the customer. |
|TotalCharges | Total charges paid by the customer over the tenure. |
|Churn | 	Binary flag indicating if the customer churned (1 = Yes, 0 = No)|

## Conclusion
From the Exploratory Data Analysis (EDA), it was observed that the key features influencing customer churn include:
- **Tenure**: Customers with longer tenure are less likely to churn.
- **Monthly Charges**: Higher charges seem to correlate with higher churn.
- **Total Charges**: Customers with higher total charges tend to churn less.
- **Service Types**: Customers with fiber optic internet services tend to have higher charges.

Coming to the machine learning models,I have used classification models - Logistic Regression,K-Nearest Neighbors (KNN),Naive Bayes (BernoulliNB),Support Vector Machine (SVM).The SVM performed better than other models
with an accuracy of 75.76%.
