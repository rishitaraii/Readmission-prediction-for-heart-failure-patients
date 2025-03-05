# Readmission Prediction for Heart Failure Patients (AI/ML)

## Project Overview
Heart failure is a major health concern, leading to frequent hospital readmissions. Predicting whether a patient will be readmitted within 30 days of discharge can help healthcare providers take preventive measures, reducing mortality rates and financial burdens on patients and hospitals. This project aims to develop a machine learning model to predict such readmissions.

## Dataset & Sources
The dataset used for this project is derived from **MIMIC-III**, a publicly available critical care database. It includes patient records, diagnoses, treatment history, and other medical parameters.

- **Diagnosis Codes (ICD-9) for Heart Failure**: ('39891', '40201', '40211', '40291', '40401', '40403', '40411', '40413', '40491', '40493', '4280', '4281', '42820', '42821', '42822', '42823', '42830', '42831', '42832', '42833', '42840', '42841', '42842', '42843', '4289')

- **MIMIC-III Table Descriptions**: [Link to documentation](https://mimic.mit.edu/docs/iii/tables/)
- **Subset of tables provided for Veersa Hackathon 2025** (OneDrive link shared by organizers)

## Data Preprocessing
Preprocessing is a crucial step in machine learning, ensuring data quality and preparing it for model training. Below are the key steps followed:

### **1. Data Loading & Exploration**
- Loaded the required MIMIC-III tables into a pandas DataFrame.
  
  

### **2. Handling Missing Values**
- Identified missing values in important features.
- Applied strategies such as **mean/median imputation**, **removal of columns with excessive missing data**, and **forward-filling for time-series data**.

  

### **3. Feature Engineering**
- Created new features such as:
- **Length of hospital stay**
- **Number of past admissions**
- **Comorbidity index**
- Encoded categorical variables using **One-Hot Encoding** and **Label Encoding**.
- Scaled numerical features using **StandardScaler**.
  

### **4. Data Splitting**
- Split the dataset into **train (80%) and test (20%)** sets for model training.
- Applied **stratified sampling** to maintain class distribution.

## Data Visualizations & Insights
To better understand the dataset, we generated the following visualizations:
- **Distribution of Readmissions**
- **Correlation Heatmap of Features**
- **Missing Value Heatmap**
- **Boxplots for Outlier Detection**

> 📌 *Images are saved in the `images/` directory.* Example:
> ```md
> ![Data Distribution](images/data_distribution.png)
> ```

## Next Steps
1. **Model Development**: Train and evaluate different ML models (Logistic Regression, Random Forest, XGBoost, etc.).
2. **Hyperparameter Tuning**: Optimize models using Grid Search & Random Search.
3. **Model Evaluation**: Use metrics like **Accuracy, Precision, Recall, F1-Score, AUC-ROC Curve**.
4. **Deployment**: Build a **Streamlit-based Admin Dashboard** for hospitals to monitor predictions.

