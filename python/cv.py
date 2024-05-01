import os
from pytesseract import Output, pytesseract
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# Path to the dataset directory
dataset_dir = r"C:\Users\gezhi\Downloads\archive (1)\train_val_images\train_images"

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



# Function to preprocess the image
def preprocess_image(image_path): 
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Perform thresholding or other preprocessing steps if needed
    return gray

# Function to extract text from the image using Tesseract
def extract_text(image_path):
    custom_config = r'--oem 3 --psm 6'  # Tesseract OCR configuration
    return pytesseract.image_to_string(image_path, config=custom_config)

# Load dataset and preprocess images
images = []
labels = []

for filename in os.listdir(dataset_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(dataset_dir, filename)
        preprocessed_image = preprocess_image(image_path)
        images.append(preprocessed_image)
        labels.append(extract_text(image_path))

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Feature extraction using Bag of Words (BOW)
vectorizer = CountVectorizer(analyzer='word')
X_train_features = vectorizer.fit_transform([' '.join(text.split()) for text in y_train])
X_test_features = vectorizer.transform([' '.join(text.split()) for text in y_test])

# Train a Support Vector Machine (SVM) classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_features, y_train)

# Evaluate the model
y_pred = svm_classifier.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the model if needed
# from joblib import dump
# dump(svm_classifier, 'ocr_model.joblib')
