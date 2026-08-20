# FORESIGHT
## AI-Powered Demand Forecasting & Inventory Intelligence

## 1. Introduction

FORESIGHT is an AI-powered demand forecasting and inventory intelligence platform developed to help businesses make better inventory planning decisions.

The system uses historical sales, inventory, pricing, promotion, weather, and seasonal information to predict product demand and identify potential inventory risks.

The project also provides an interactive Streamlit dashboard for analyzing demand forecasts, inventory risks, recommendations, and model performance.

---

## 2. Problem Statement

Maintaining the correct inventory level is an important challenge for businesses.

Insufficient inventory can lead to stockouts and lost sales, while excessive inventory can increase storage costs and result in unsold products.

FORESIGHT addresses this problem by using machine learning to forecast demand and compare predicted demand with current inventory levels.

---

## 3. Objectives

The main objectives of the project are:

- Analyze historical sales and inventory data.
- Clean and preprocess the dataset.
- Perform exploratory data analysis.
- Build a machine learning model for demand forecasting.
- Evaluate model performance.
- Identify stockout and overstock risks.
- Generate inventory recommendations.
- Build an interactive dashboard.
- Provide a simple interface for business users.

---

## 4. Dataset

The dataset contains 76,000 records and 16 original columns.

Important features include:

- Store ID
- Product ID
- Category
- Region
- Inventory Level
- Units Sold
- Units Ordered
- Price
- Discount
- Weather Condition
- Promotion
- Competitor Pricing
- Seasonality
- Epidemic
- Demand

The dataset was processed and prepared for machine learning.

---

## 5. Data Preprocessing

The following preprocessing steps were performed:

- Dataset loading
- Missing-value checking
- Duplicate checking
- Categorical feature encoding
- Date processing
- Feature extraction
- Conversion of categorical values into numerical representations
- Preparation of training and testing data

Date-related features such as Year, Month, Day, and DayOfWeek were extracted.

---

## 6. Exploratory Data Analysis

Exploratory data analysis was performed to understand relationships between inventory, sales, pricing, and demand.

Visualizations were created to identify patterns and trends in the dataset.

The analysis helped determine which variables could be useful for demand forecasting.

---

## 7. Machine Learning Model

A Random Forest Regressor was selected for demand forecasting.

The model was trained using the processed dataset and evaluated on test data.

The target variable used for prediction was:

Demand

---

## 8. Model Evaluation

The model achieved the following results:

| Metric | Result |
|---|---:|
| MAE | 12.76 |
| MSE | 289.38 |
| RMSE | 17.01 |
| R² Score | 0.869 |

The R² score indicates that the model explains approximately 86.9% of the variation in demand on the evaluated test dataset.

---

## 9. Feature Importance

The Random Forest model identified the following important features:

1. Units Sold
2. Units Ordered
3. Inventory Level
4. Price
5. Competitor Pricing
6. Day
7. Category
8. Product ID
9. Month
10. DayOfWeek

Units Sold was the most influential feature in the trained model.

---

## 10. Inventory Risk Analysis

The system compares inventory levels with predicted demand.

Three risk categories were created.

### Stockout Risk

When available inventory is lower than expected demand, the system identifies a potential stockout risk.

Recommendation:

**Reorder Stock**

### Overstock Risk

When inventory is considerably higher than expected demand, the system identifies a potential overstock risk.

Recommendation:

**Offer Discount / Reduce Orders**

### Healthy Inventory

When inventory is within an appropriate range compared with predicted demand:

**No Action Required**

---

## 11. Dashboard

A Streamlit dashboard was developed to make the results easy to understand.

The dashboard includes:

- KPI cards
- Inventory statistics
- Predicted demand
- Risk distribution
- Inventory vs predicted demand
- Risk analysis
- Inventory recommendations
- Model performance
- Interactive filters
- CSV download functionality

---

## 12. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- GitHub

---

## 13. Project Structure

```text
project_foresight/
│
├── models/
├── data/
├── app/
├── screenshots/
├── notebooks/
├── risk_analysis.csv
├── streamlit_app.py
├── requirements.txt
├── README.md
└── FINAL_REPORT.md

##14. Demo

Live Dashboard:

[https://projectforesight-zcz83s6nilwdajezltjbz7.streamlit.app/]

GitHub Repository:

[https://github.com/khaleeq-bit/project_foresight]

##15. Screenshots

Screenshots of the working dashboard are included in the project repository.


##16. Challenges Faced

During development, several challenges were encountered, including:

Handling categorical data for machine learning.
Resolving file-path issues.
Saving and loading the trained machine learning model.
Handling project folder organization.
Creating inventory risk calculations.
Connecting the trained model with the Streamlit dashboard.
Preparing the project for deployment.

These challenges helped improve practical understanding of machine learning project development and deployment.

##17. What I Learned

Through this project, I learned:

How to work with a large dataset.
How to perform data preprocessing.
How to perform exploratory data analysis.
How to train a Random Forest regression model.
How to evaluate a machine learning model.
How to analyze feature importance.
How to convert predictions into business insights.
How to perform inventory risk analysis.
How to build an interactive Streamlit dashboard.
How to organize a machine learning project.
How to use GitHub for project submission.
How to deploy a machine learning application.


##18. Future Scope

Future improvements could include:

Advanced time-series forecasting.
Real-time inventory data integration.
Automated stock alerts.
Automated data updates.
More advanced inventory optimization.
Cloud database integration.
Integration with business ERP systems.
Improved forecasting using deep learning models.


##19. Conclusion

FORESIGHT combines machine learning, demand forecasting, inventory risk analysis, and data visualization into a single platform.

The Random Forest model achieved an R² score of 0.869 on the evaluated test data.

The system converts demand predictions into practical inventory recommendations and presents the results through an interactive Streamlit dashboard.

The project demonstrates how machine learning can be applied to a practical business problem and transformed into a usable decision-support application.

---

## 20. Final Submission

This repository represents the final submission of the FORESIGHT project.

The project includes the complete source code, trained machine learning model, data processing workflow, inventory risk analysis, interactive Streamlit dashboard, documentation, screenshots, and deployment information.

The application was tested locally and deployed successfully for demonstration.