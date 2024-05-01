import cv2
import pytesseract

# Path to Tesseract executable (change this according to your installation)

def find_thickest_word(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(gray_image)

    # Split the extracted text into words
    word = extracted_text.split()
    return word

# Replace 'image_path' with the path to your image
image_path = r"C:\Users\gezhi\Downloads\WhatsApp Image 2024-03-15 at 11.07.21 PM.jpeg"
word = find_thickest_word(image_path)
print(word)
