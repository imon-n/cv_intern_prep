
# 🧪 Task 2 — Webcam + FPS using Python + OpenCV

## Question

Write a Python program using OpenCV to access the computer's webcam and display the live video stream. The program should calculate and display the approximate FPS (Frames Per Second) on the video frame. The program should continue running until the user presses the `Q` key. After exiting, release the webcam and properly close all OpenCV windows.

---

## Code

```python
import cv2
import time

# Open the default webcam
# 0 = first/default camera
cap = cv2.VideoCapture(0)

# Store the previous time
# We need this to calculate the time between two frames
prev_time = time.time()

while True:

    # Read one frame from the webcam
    # ret = whether frame was captured successfully
    # frame = actual webcam image
    ret, frame = cap.read()

    # Check if frame was captured successfully
    if not ret:
        print("Failed to read frame")
        break

    # Get current time
    current_time = time.time()

    # Calculate FPS
    # FPS = number of frames per second
    fps = 1 / (current_time - prev_time)

    # Update previous time
    prev_time = current_time

    # Display FPS on the frame
    cv2.putText(
        frame,                         # Image where text will be written
        f"FPS: {fps:.2f}",             # Text to display
        (20, 40),                      # Text position: x=20, y=40
        cv2.FONT_HERSHEY_SIMPLEX,      # Font type
        1,                             # Font size
        (0, 255, 0),                  # Color: Green (BGR)
        2                              # Text thickness
    )

    # Display webcam frame
    cv2.imshow("Webcam", frame)

    # Wait for keyboard input
    # 1 = wait approximately 1 millisecond
    # ord("q") = Q key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
````

---

# Possible Questions & Answers

## 1. Which libraries did you use?

**Answer:**

I used `OpenCV` for webcam and image processing, and Python's `time` library for calculating FPS.

---

## 2. Why do you use OpenCV?

**Answer:**

OpenCV is used for computer vision, image processing, video processing, webcam access, object detection, and many other CV tasks.

---

## 3. What does `cv2.VideoCapture(0)` do?

**Answer:**

It opens the default webcam.

```python
cap = cv2.VideoCapture(0)
```

`0` usually means the first camera.

---

## 4. What does `cap.read()` do?

**Answer:**

It captures one frame from the webcam and returns two values: `ret` and `frame`.

```python
ret, frame = cap.read()
```

---

## 5. What is `ret`?

**Answer:**

`ret` tells us whether the frame was captured successfully.

* `True` → frame captured successfully
* `False` → frame capture failed

---

## 6. What is `frame`?

**Answer:**

`frame` contains the actual image captured from the webcam.

---

## 7. Why do you use `while True`?

**Answer:**

Because we need to continuously capture and process webcam frames in real time.

---

## 8. What is FPS?

**Answer:**

FPS means **Frames Per Second**. It represents how many frames are processed or displayed per second.

---

## 9. Why is FPS important?

**Answer:**

FPS helps us understand the performance and smoothness of a real-time video application.

---

## 10. How do you calculate FPS?

**Answer:**

```python
fps = 1 / (current_time - prev_time)
```

It calculates the approximate number of frames processed per second.

---

## 11. Why do you use `time.time()`?

**Answer:**

`time.time()` gives the current time in seconds. We use it to measure the time difference between consecutive frames.

---

## 12. What does this line do?

```python
prev_time = time.time()
```

**Answer:**

It stores the current time as the previous timestamp, which is needed for FPS calculation.

---

## 13. What does `cv2.putText()` do?

**Answer:**

It writes text directly on an image or video frame.

---

## 14. Explain the parameters of `cv2.putText()`.

**Answer:**

```python
cv2.putText(
    frame,
    f"FPS: {fps:.2f}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
```

```text
frame                      → Image/frame
f"FPS: {fps:.2f}"          → Text
(20, 40)                   → Text position
FONT_HERSHEY_SIMPLEX      → Font
1                          → Font size
(0, 255, 0)               → Green color
2                          → Thickness
```

---

## 15. What does `{fps:.2f}` mean?

**Answer:**

It displays the FPS value with **2 digits after the decimal point**.

For example:

```text
FPS: 29.57
```

---

## 16. Why `(20, 40)`?

**Answer:**

It specifies the position of the text.

```text
20 → x-coordinate
40 → y-coordinate
```

So the text starts approximately 20 pixels from the left and 40 pixels from the top.

---

## 17. What does `(0, 255, 0)` mean?

**Answer:**

It represents green in OpenCV's **BGR** color format.

```text
B = 0
G = 255
R = 0
```

---

## 18. What does `cv2.imshow()` do?

**Answer:**

It displays an image or video frame in an OpenCV window.

---

## 19. What does `cv2.waitKey(1)` do?

**Answer:**

It waits briefly for a keyboard event and allows the OpenCV window to update.

---

## 20. Why do you use `ord("q")`?

**Answer:**

`ord("q")` converts the character `q` into its corresponding integer character code so it can be compared with the key returned by `waitKey()`.

---

## 21. How does pressing Q stop the program?

**Answer:**

This condition checks whether the user pressed `q`:

```python
if cv2.waitKey(1) & 0xFF == ord("q"):
    break
```

If true, `break` exits the `while` loop.

---

## 22. Why do you use `cap.release()`?

**Answer:**

It releases the webcam resource after the program finishes.

---

## 23. Why do you use `cv2.destroyAllWindows()`?

**Answer:**

It closes all OpenCV windows.

---

## 24. What happens if `ret` is False?

**Answer:**

It means the frame could not be captured successfully, so we stop the loop using `break`.

---

## 25. Can `VideoCapture()` read a video file?

**Answer:**

Yes.

```python
cap = cv2.VideoCapture("video.mp4")
```

The same `VideoCapture` class can be used for webcams and video files.

---

## 26. How can you access another camera?

**Answer:**

You can change the camera index.

```python
cap = cv2.VideoCapture(1)
```

`1` usually represents the second connected camera.

---

## 27. What happens if FPS becomes very low?

**Answer:**

The video may become less smooth. Possible causes include high-resolution processing, heavy computer-vision operations, CPU limitations, or slow camera input.

---

## 28. How can you improve real-time FPS?

**Answer:**

We can reduce resolution, process fewer frames, optimize the algorithm, use a smaller AI model, or use GPU acceleration when available.

---

# ⭐ Important Values to Remember

| Value                  | Meaning                       |
| ---------------------- | ----------------------------- |
| `cv2`                  | OpenCV library                |
| `time`                 | Python time library           |
| `VideoCapture(0)`      | Open default webcam           |
| `0`                    | First camera                  |
| `ret`                  | Frame capture success/failure |
| `frame`                | Current webcam image          |
| `time.time()`          | Current timestamp             |
| `FPS`                  | Frames Per Second             |
| `(20, 40)`             | Text position                 |
| `FONT_HERSHEY_SIMPLEX` | Text font                     |
| `1`                    | Font size                     |
| `(0, 255, 0)`          | Green color in BGR            |
| `2`                    | Text thickness                |
| `waitKey(1)`           | Short keyboard wait           |
| `ord("q")`             | Character code of `q`         |
| `cap.release()`        | Release webcam                |
| `destroyAllWindows()`  | Close OpenCV windows          |

---

# ⭐ Most Important Interview Questions

If the interviewer asks quickly, remember these:

### What does `VideoCapture(0)` do?

**It opens the default webcam.**

### What is `ret, frame = cap.read()`?

**It captures one webcam frame and tells us whether the capture was successful.**

### What is FPS?

**Frames Per Second — the number of frames processed/displayed per second.**

### How do you calculate FPS?

**FPS is approximately `1 / time_taken_per_frame`.**

### Why use `cv2.putText()`?

**To display information such as FPS directly on the video frame.**

### Why use `waitKey(1)`?

**To process keyboard input and allow the video window to update.**

### Why `ord("q")`?

**To detect when the user presses the Q key.**

### Why `cap.release()`?

**To release the webcam resource.**

### Why `destroyAllWindows()`?

**To close all OpenCV windows.**

---

# ⭐ Complete Webcam Pipeline

```text
Webcam
   ↓
VideoCapture(0)
   ↓
Read Frame
   ↓
Check ret
   ↓
Calculate FPS
   ↓
Put FPS on Frame
   ↓
Display Frame
   ↓
Press Q?
   ↓
Release Camera
   ↓
Close Windows
```
