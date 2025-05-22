UCI Heart Disease Prediction Project - User Guide
==================================================

About the Project
-----------------
This project is an application for predicting heart disease risk using the UCI Heart Disease dataset with machine learning and advanced data processing techniques. The best model (LightGBM) was selected, and a web interface was created so users can enter their own data and get predictions.

Setup and Requirements
----------------------
1. Python 3.8 or higher
2. Required libraries:
   - streamlit
   - numpy
   - pandas
   - scikit-learn
   - lightgbm
   - joblib
   - imbalanced-learn

Running the Web Interface
-------------------------
1. Go to the project folder in your terminal or command prompt:

    cd c:...\UCI_heart_disease

2. Start the web application:

    streamlit run web.py

3. In the browser window that opens, fill in the required information and click the "Predict" button. The results will be displayed on the screen.


How to Use the Web Interface
----------------------------
You need to enter the following information in the web interface:
- ST Depression (st_depression)
- Exercise Induced Angina (exercise_induced_angina)
- Age (age)
- Sex (sex_Male)
- Resting ECG Results: ST-T Abnormality (resting_ecg_results_st-t abnormality)
- Fasting Blood Sugar > 120 mg/dl? (fasting_blood_sugar)
- Resting Blood Pressure (resting_blood_pressure)
- Chest Pain Type: Non-anginal (chest_pain_type_non-anginal)
- Resting ECG Results: Normal (resting_ecg_results_normal)
- Serum Cholesterol (serum_cholesterol)
- Chest Pain Type: Atypical Angina (chest_pain_type_atypical angina)
- Max Heart Rate Achieved (thalch)

Enter the appropriate value for each field and click the predict button. Your heart disease risk and the model's confidence will be displayed.

Code Usage and Customization
----------------------------
- Model and data processing steps are explained in detail in the `uci_code.ipynb` file.
- The web interface code is in `web.py`. Feature names and order must match those used during model training.
- The model file (`best_heart_disease_model.joblib`) and dataset (`heart_disease_uci.csv`) must be present in the project folder.

Notes
-----
- This application should not be used for medical diagnosis. Results are based solely on a machine learning model.
- If you have questions or encounter errors, review your code and data processing steps.


For details, see `uci_code.ipynb` (data processing, model training) and `web.py` (web interface).

---

Project Owner: [Kerem Akgöz]
Date: May 2025
