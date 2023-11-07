import cv2
import numpy as np

# Load the pre-trained Haar Cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Iterate through detected eyes
    for (ex, ey, ew, eh) in eyes:
        eye_roi = gray[ey:ey+eh, ex:ex+ew]  # Region of interest for the eye

        # Apply Hough Circle Transform to detect the pupils
        circles = cv2.HoughCircles(eye_roi, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
                                   param1=200, param2=10, minRadius=5, maxRadius=15)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                x, y, r = circle
                # Draw the circle around the pupil
                cv2.circle(frame, (ex + x, ey + y), r, (0, 0, 255), 2)
                # Calculate the direction in degrees
                direction_x = ex + x - (ex + ew // 2)
                direction_y = ey + y - (ey + eh // 2)
                angle = np.arctan2(direction_y, direction_x)
                angle_degrees = np.degrees(angle)
                # Display the direction text on the frame
                cv2.putText(frame, f"Direction: {angle_degrees:.2f}", (ex, ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with eye detection and direction
    cv2.imshow('Eye Direction Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
