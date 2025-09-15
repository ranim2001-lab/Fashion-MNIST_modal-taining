import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Load model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/trained_fashion_mnist_model.h5"
model = tf.keras.models.load_model(model_path)

# Class labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Preprocess function
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((28, 28))
    img = img.convert('L')  # Grayscale
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array

# Streamlit UI
st.set_page_config(page_title="Fashion MNIST Classifier", layout="wide")
st.title("👗 Fashion Item Classifier")

st.sidebar.header("Instructions")
st.sidebar.write("""
1. Upload an image of a clothing item.
2. Click the **Classify** button.
3. See the predicted category.
""")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, width=200)

    with col2:
        st.subheader("Prediction")
        if st.button('Classify'):
            with st.spinner('Classifying...'):
                img_array = preprocess_image(uploaded_image)
                result = model.predict(img_array)
                predicted_class = np.argmax(result)
                prediction = class_names[predicted_class]
                st.success(f'Prediction: **{prediction}**')
                

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using **TensorFlow** and **Streamlit**")
