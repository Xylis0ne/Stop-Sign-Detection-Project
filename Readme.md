# Stop Sign Detection Project

## Overview

This project uses Python and the OpenCV library to detect stop signs in images, showcasing the application of computer vision techniques. It identifies stop signs by converting images to the RGB color space and applying a pre-trained cascade classifier, then highlights detected stop signs with a green rectangle.

## Features

- Utilizes OpenCV for image processing.
- Employs cascade classifiers for stop sign detection.
- Leverages matplotlib for visualizing detection results.

## Installation

Ensure Python 3.6 or later is installed on your system. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

To set up this project:

1. Clone the repository:
    ```bash
    git clone https://github.com/mohammedz1ane/Stop-Sign-Detection-Project.git
    ```

2. Navigate to the project directory:
    ```bash
    cd stop-sign-detection
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your images in the `images` folder. Name the images `image.jpg`, `image2.jpg`, and `image3.jpg`.
2. Run the script:
    ```bash
    python3 stop_sign_detection.py
    ```

The script processes the images and displays them with detected stop signs marked.

## How It Works

The project leverages OpenCV's `CascadeClassifier` to detect stop signs. It first converts images from BGR to RGB for accurate color representation in matplotlib, then scans for stop sign patterns, marking detected signs with rectangles.

## Limitations

- Detection accuracy is affected by the quality and angle of the stop signs.
- Designed for a predefined set of images; future versions could support dynamic image input.
