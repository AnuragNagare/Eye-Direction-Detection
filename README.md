# Eye Direction Detection using OpenCV and Python

![Demo](demo.gif)

This project demonstrates how to use OpenCV and Python to detect the direction of a person's gaze by identifying and tracking their eyes. It can be used in a wide range of applications, including assistive technology for people with limited mobility and improving user experiences in human-computer interaction.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3
- OpenCV
- NumPy

You can install the necessary Python packages using pip:
pip install opencv-python numpy

How it Works
The code uses a pre-trained Haar Cascade classifier to detect eyes in the webcam feed.
For each detected eye, it applies the Hough Circle Transform to find the pupils' positions.
It calculates the direction of the gaze based on the pupils' positions.
The direction is displayed on the video feed in real-time.
Usage
Run the script and look at the webcam.
The code will display the direction of your gaze in degrees on the video feed.



https://github.com/AnuragNagare/Eye-Direction-Detection/assets/85473989/c6063325-d709-4893-b68e-774c3894e60e



