# Fashion-MNIST Modal Training

This project is a **Fashion Item Classifier** built using **TensorFlow** and **Streamlit**. The classifier predicts fashion items from images using a pre-trained model on the **Fashion MNIST dataset**.

---

## Features

- Classify images of clothing items into 10 categories:
  - T-shirt/top
  - Trouser
  - Pullover
  - Dress
  - Coat
  - Sandal
  - Shirt
  - Sneaker
  - Bag
  - Ankle boot
- Upload images via a simple **Streamlit web interface**
- View predictions in real-time
- Pre-trained model included (`trained_fashion_mnist_model.h5`)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ranim2001-lab/Fashion-MNIST_modal-taining.git
cd Fashion-MNIST_modal-taining/app

2. Create a virtual environment (recommended):

conda create -n fashion python=3.10 -y
conda activate fashion


3. Install required dependencies:

pip install -r requirements.txt![Uploading preuve.PNG…]()


## 📸 Screensh


🏃‍♂️ Usage

Run the Streamlit app:

streamlit run main.py


Open the URL in your browser (default: http://localhost:8501)

Upload a fashion image and click Classify to see the result

🗂 Project Structure
fashion-mnist-end-to-end-project/
├── app/
│   ├── main.py                # Streamlit application
│   ├── requirements.txt       # Required Python packages
│   └── trained_model/
│       └── trained_fashion_mnist_model.h5
├── model_training_notebook/
│   └── Fashion_MNIST_modal_taining.ipynb
└── test_images/               # Sample test images

Technologies

Python 3.10

TensorFlow 2.x

Streamlit

NumPy

PIL (Python Imaging Library)
