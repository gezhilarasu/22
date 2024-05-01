import cv2
import pytesseract

# Step 3: Read the Image
image = cv2.imread('kk.png')

# Step 4: Preprocess the Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply any necessary preprocessing steps here

# Step 5: Apply OCR using Tesseract
text = pytesseract.image_to_string(gray_image)

# Step 6: Display or Use the Extracted Text
print(text)
