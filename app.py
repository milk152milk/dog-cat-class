import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Set page config
st.set_page_config(page_title="Dog vs Cat Classifier", page_icon="🐾", layout="centered")

st.title("🐾 Dog vs Cat Image Classifier")
st.write("Upload an image of a dog or a cat, and the Xception model will predict which one it is!")

@st.cache_resource
def load_classification_model():
    """Load the pre-trained Xception model."""
    import os
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    return tf.keras.models.load_model('best_model_xception.keras')

try:
    with st.spinner("Loading model from disk..."):
        model = load_classification_model()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    
    # Display the image centered
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("---")
    with st.spinner("Classifying image..."):
        try:
            # Dynamically determine the target size based on model input shape
            input_shape = model.input_shape
            if input_shape[1] is not None and input_shape[2] is not None:
                target_size = (input_shape[1], input_shape[2])
            else:
                target_size = (299, 299)
        except:
            target_size = (299, 299)
            
        # Convert image to RGB
        if image.mode != "RGB":
            image = image.convert("RGB")
            
        # Resize image
        img = image.resize(target_size)
        
        # Convert to numpy array
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Xception preprocessing (scale pixels between -1 and 1)
        img_array = tf.keras.applications.xception.preprocess_input(img_array)

        # Make prediction
        predictions = model.predict(img_array)
        
        # Analyze the prediction shape to map results accurately
        result = ""
        prediction_shape_len = predictions.shape[-1]
        
        if prediction_shape_len == 1:
            probability = float(predictions[0][0])
            if probability > 0.5:
                result = f"**🐶 Dog** (Confidence: {probability:.2%})"
            else:
                result = f"**🐱 Cat** (Confidence: {(1 - probability):.2%})"
                
        elif prediction_shape_len == 2:
            class_idx = np.argmax(predictions[0])
            probability = float(predictions[0][class_idx])
            if class_idx == 0:
                result = f"**🐱 Cat** (Confidence: {probability:.2%})"
            else:
                result = f"**🐶 Dog** (Confidence: {probability:.2%})"
        else:
            result = f"Unknown model output format: {predictions.shape}. Raw: {predictions[0]}"

        # Display Result
        st.subheader("Prediction Result")
        st.info(result)
