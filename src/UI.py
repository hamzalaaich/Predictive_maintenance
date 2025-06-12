# streamlit_app.py
import streamlit as st
import requests
import pandas as pd
from PIL import Image

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RUL Predictor", page_icon="🔧", layout="centered")
st.title("🔧 Remaining Useful Life (RUL) Prediction")
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stRadio > div {
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

option = st.radio("🔘 Choose prediction type:", ("Single Prediction", "Batch Prediction"))

# Only the features used in training
reduced_feature_list = [
    'setting_1', 'setting_2', 'setting_3',
    's_2', 's_3', 's_4', 's_7', 's_8',
    's_9', 's_11', 's_12', 's_13', 's_15', 's_17'
]

if option == "Single Prediction":
    st.subheader("🔍 Predict for a Single Instance")
    single_input = {}
    for feature in reduced_feature_list:
        single_input[feature] = st.number_input(f"{feature}", value=0.0)

    if st.button("🚀 Predict RUL"):
        with st.spinner("Sending data to API..."):
            response = requests.post(f"{API_URL}/predict", json=single_input)
        if response.status_code == 200:
            st.success(f"✅ Predicted RUL: {response.json()['predicted_rul']:.2f} cycles")
        else:
            st.error(f"❌ Error: {response.text}")

else:
    st.subheader("📂 Predict for a CSV File")
    uploaded_file = st.file_uploader("Upload a CSV file with the required columns", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        if st.button("📈 Batch Predict"):
            payload = {"data": df[reduced_feature_list].to_dict(orient="records")}
            with st.spinner("Sending data to API..."):
                response = requests.post(f"{API_URL}/batch_predict", json=payload)
            if response.status_code == 200:
                df["Predicted_RUL"] = response.json()["predictions"]
                st.success("✅ Prediction completed")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Download Predictions as CSV", csv, "predicted_rul.csv", "text/csv")
            else:
                st.error(f"❌ Error: {response.text}")
