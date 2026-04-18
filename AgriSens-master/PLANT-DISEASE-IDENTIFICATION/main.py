import streamlit as st
import numpy as np
import os   # add this

# 👇 BASE PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# FIXED MODEL FUNCTION
# =========================
def model_prediction(test_image):
    return None   # TensorFlow removed → no prediction

#Sidebar
st.sidebar.title("AgriSens")
app_mode = st.sidebar.selectbox("Select Page",["HOME","DISEASE RECOGNITION"])

# import Image from pillow to open images
from PIL import Image

# Build full path to image
image_path = os.path.join(BASE_DIR, "Diseases.png")

img = Image.open(image_path)
st.image(img)

#Main Page
if(app_mode=="HOME"):
    st.markdown("<h1 style='text-align: center;'>SMART DISEASE DETECTION", unsafe_allow_html=True)
    
#Prediction Page
elif(app_mode=="DISEASE RECOGNITION"):
    st.header("DISEASE RECOGNITION")

    st.warning("⚠️ Model works only locally (TensorFlow not supported in deployment)")

    test_image = st.file_uploader("Choose an Image:")

    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)

    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")

        result_index = model_prediction(test_image)

        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']

        # ✅ FIX HERE
        if result_index is None:
            st.error("⚠️ Prediction not available in deployed version. Run locally for full functionality.")
        else:
            st.success("Model is Predicting it's a {}".format(class_name[result_index]))

            predicted_class = class_name[result_index]

            # ==========================================
            # Fertilizer & Pesticide Suggestions
            # ==========================================
            recommendation = {
                'Apple___Apple_scab':{
                    "fertilizer":"Apply balanced NPK (10-10-10) and increase potassium.",
                    "pesticide":"Spray Captan or Mancozeb fungicide every 7 days."
                }
                # (keep your full dictionary same)
            }

            fert = recommendation[predicted_class]["fertilizer"]
            pest = recommendation[predicted_class]["pesticide"]

            st.subheader("🌱 Fertilizer Recommendation")
            st.info(fert)

            st.subheader("🧪 Pesticide Recommendation")
            st.warning(pest)
