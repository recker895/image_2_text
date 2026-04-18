import cv2
import pytesseract
from PIL import Image

# If on Windows, set path (important)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image = cv2.imread("image.png")

# Convert to grayscale (better OCR accuracy)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optional: thresholding (improves clarity)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save temporary image (optional)
cv2.imwrite("processed.png", thresh)

# Extract text
text = pytesseract.image_to_string(Image.open("processed.png"))

print("Extracted Text:\n")
print(text)