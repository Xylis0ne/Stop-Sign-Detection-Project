import cv2
from matplotlib import pyplot as plt

# Function to convert BGR images to RGB
def convert_bgr_to_rgb(images):
    return [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in images]

# Load images from 'images' folder
image_files = ["images/image.jpg", "images/image2.jpg", "images/image3.jpg"]
images = [cv2.imread(file) for file in image_files]

# Convert images to RGB for displaying with matplotlib
images_rgb = convert_bgr_to_rgb(images)

# Initialize the Cascade Classifier for stop sign detection
stop_data = cv2.CascadeClassifier('stop_data.xml')

# Function to detect and mark stop signs in images
def detect_stop_signs(images_rgb):
    for img_rgb in images_rgb:
        found = stop_data.detectMultiScale(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY), minSize=(20, 20))
        for (x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 5)

# Detect and mark stop signs in the images
detect_stop_signs(images_rgb)

# Display the images side by side
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ['Image 1', 'Image 2', 'Image 3']
for ax, img, title in zip(axes, images_rgb, titles):
    ax.imshow(img)
    ax.set_title(title)
plt.show()
