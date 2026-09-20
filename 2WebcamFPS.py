import cv2
import time

# Open the default webcam
# 0 means the first/default camera connected to the computer
cap = cv2.VideoCapture(0)

# Store the starting time
prev_time = time.time()

while True:

    # Read one frame from the webcam
    ret, frame = cap.read()

    # Check whether the frame was captured successfully
    if not ret:
        print("Failed to read frame")
        break

    # Get the current time
    current_time = time.time()

    # Calculate FPS
    fps = 1 / (current_time - prev_time)

    # Update previous time
    prev_time = current_time

    # Display FPS on the frame
    cv2.putText(
        frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    # cv2.putText(image, text, position, font, size, color, thickness)

    # Display webcam frame
    cv2.imshow("Webcam", frame)

    # Wait for a key
    # ord("q") means the Q key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()