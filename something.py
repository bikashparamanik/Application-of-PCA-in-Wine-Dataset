import cv2
import numpy as np

# Load JPEG image
image_path = r"D:\anantadi\Advertisement Image.jpg"
jpeg_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if jpeg_image is None:
    print("Error: Unable to load the image.")
    exit()

# Convert white background to transparency
gray_image = cv2.cvtColor(jpeg_image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)

png_image = cv2.cvtColor(jpeg_image, cv2.COLOR_BGR2BGRA)
png_image[:, :, 3] = mask

# Save as PNG image with a proper file path
cv2.imwrite(r"D:\anantadi\Advertisement_Image_with_transparency.png", png_image)
