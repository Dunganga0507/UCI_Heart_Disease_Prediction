import streamlit as st
import joblib
import numpy as np

# Türkçe Açıklama:
# Bu uygulama, kullanıcının girdiği bilgilere göre kalp hastalığı riskini tahmin eder.
# Model, UCI Heart Disease veri seti üzerinde eğitilmiş ve en iyi sonuç veren model kaydedilmiştir.

# English Explanation:
# This app predicts the risk of heart disease based on user input.
# The model was trained on the UCI Heart Disease dataset and the best performing model was saved.

# Modeli yükle / Load the trained model
model = joblib.load('best_heart_disease_model.joblib')

# Özellik isimleri (modelin beklediği sırada) / Feature names in the order expected by the model
feature_names = [
    'age', 'resting_blood_pressure', 'serum_cholesterol', 'fasting_blood_sugar',
    'resting_ecg_results', 'max_heart_rate_achieved', 'exercise_induced_angina',
    'st_depression', # ... diğer önemli özellikler (modelinizin beklediği sırada)
]

# Streamlit başlığı / Streamlit title
st.title("Kalp Hastalığı Riski Tahmin Uygulaması")
st.write("Aşağıdaki bilgileri doldurun ve kalp hastalığı riskinizi öğrenin.")

# Kullanıcıdan veri al / Get user input
st_depression = st.number_input("ST Depresyonu / ST Depression", min_value=0.0, max_value=10.0, value=1.0)
exercise_induced_angina = st.selectbox("Egzersizle Oluşan Angina / Exercise Induced Angina", [0, 1])
age = st.number_input("Yaş / Age", min_value=18, max_value=100, value=50)
sex_Male = st.selectbox("Cinsiyet / Sex (Erkek için 1, Kadın için 0)", [0, 1])
resting_ecg_results_st_t_abnormality = st.selectbox("İstirahat EKG Sonucu: ST-T Anormalliği / Resting ECG Results: ST-T Abnormality", [0, 1])
fasting_blood_sugar = st.selectbox("Açlık Kan Şekeri > 120 mg/dl? / Fasting Blood Sugar > 120 mg/dl?", [0, 1])
resting_blood_pressure = st.number_input("İstirahat Kan Basıncı (mmHg) / Resting Blood Pressure", min_value=80, max_value=200, value=120)
chest_pain_type_non_anginal = st.selectbox("Göğüs Ağrısı Tipi: Non-anginal / Chest Pain Type: Non-anginal", [0, 1])
resting_ecg_results_normal = st.selectbox("İstirahat EKG Sonucu: Normal / Resting ECG Results: Normal", [0, 1])
serum_cholesterol = st.number_input("Serum Kolesterol (mg/dl) / Serum Cholesterol", min_value=100, max_value=600, value=200)
chest_pain_type_atypical_angina = st.selectbox("Göğüs Ağrısı Tipi: Atypical Angina / Chest Pain Type: Atypical Angina", [0, 1])
thalch = st.number_input("Maksimum Kalp Atış Hızı / Max Heart Rate Achieved (thalch)", min_value=60, max_value=220, value=150)

# Tahmin için veri vektörü oluştur / Create input vector for prediction
input_data = np.array([[st_depression, exercise_induced_angina, age, sex_Male, resting_ecg_results_st_t_abnormality,
                        fasting_blood_sugar, resting_blood_pressure, chest_pain_type_non_anginal,
                        resting_ecg_results_normal, serum_cholesterol, chest_pain_type_atypical_angina, thalch]])

# Tahmin yap / Make prediction
if st.button("Tahmin Et / Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else None

    if prediction == 1:
        st.error(f"Yüksek risk: Kalp hastalığı olasılığınız yüksek! (Risk: {probability:.2f})" if probability is not None else "Yüksek risk: Kalp hastalığı olasılığınız yüksek!")
    else:
        st.success(f"Düşük risk: Kalp hastalığı olasılığınız düşük. (Risk: {probability:.2f})" if probability is not None else "Düşük risk: Kalp hastalığı olasılığınız düşük.")

    st.write("**Not:** Bu sonuçlar yalnızca makine öğrenmesi modeline dayalıdır ve tıbbi tavsiye yerine geçmez.")