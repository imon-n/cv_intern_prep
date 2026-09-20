
````md
# 🧪 Task 1 — Image Processing with OpenCV

## Task Name

**Basic Image Processing and Canny Edge Detection using Python + OpenCV**

---

## Question

Write a Python program using OpenCV to read an image, resize it to `640 × 480`, convert it to grayscale, apply Gaussian Blur, perform Canny Edge Detection, save the result as `output_edges.jpg`, and display both the original and edge-detected images.

---

## Code

```python
import cv2

# Read the image
image = cv2.imread("football.png")

# Resize image
# 640 = width, 480 = height
image = cv2.resize(image, (640, 480))

# Convert BGR image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
# (5, 5) = kernel size
# 0 = sigma is calculated automatically
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny Edge Detection
# 50 = lower threshold
# 150 = upper threshold
edges = cv2.Canny(blur, 50, 150)

# Save the edge-detected image
cv2.imwrite("output_edges.jpg", edges)

# Display original image
cv2.imshow("Original", image)

# Display edge image
cv2.imshow("Edges", edges)

# Wait until any key is pressed
# 0 = wait indefinitely
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
````

---

# Possible Questions & Answers

## 1. Which library did you use?

**Answer:**
I used the `OpenCV` library, imported as `cv2`.

---

## 2. Why do you use OpenCV?

**Answer:**
OpenCV is used for image processing, computer vision, video processing, image reading, resizing, filtering, edge detection, and many other CV tasks.

---

## 3. What does `cv2.imread()` do?

**Answer:**
`cv2.imread()` reads an image from a file and returns it as a NumPy array.

---

## 4. What does this line do?

```python
image = cv2.imread("football.png")
```

**Answer:**
It reads the `football.png` image into memory.

---

## 5. What does `cv2.resize()` do?

**Answer:**
It changes the dimensions or resolution of an image.

---

## 6. Why did you use `(640, 480)`?

**Answer:**
It sets the image width to `640` pixels and height to `480` pixels.

```text
Width  = 640
Height = 480
```

---

## 7. What does `cv2.cvtColor()` do?

**Answer:**
It converts an image from one color space to another.

---

## 8. Why do you use `cv2.COLOR_BGR2GRAY`?

**Answer:**
OpenCV normally reads color images in BGR format. `COLOR_BGR2GRAY` converts the BGR image into grayscale.

---

## 9. Why convert the image to grayscale?

**Answer:**
Grayscale contains only intensity information, so it reduces the amount of data and makes many image-processing operations simpler and faster.

---

## 10. What is Gaussian Blur?

**Answer:**
Gaussian Blur is an image smoothing technique used to reduce noise and small unwanted details before further processing.

---

## 11. Why did you use `(5, 5)` in Gaussian Blur?

**Answer:**
`(5, 5)` is the Gaussian kernel size. It determines the neighborhood used for smoothing.

---

## 12. What does the `0` mean here?

```python
cv2.GaussianBlur(gray, (5, 5), 0)
```

**Answer:**
It means the Gaussian sigma value is calculated automatically by OpenCV.

---

## 13. Why do we apply Gaussian Blur before Canny?

**Answer:**
Gaussian Blur reduces noise. This helps Canny Edge Detection avoid detecting unnecessary noise as edges.

---

## 14. What is Canny Edge Detection?

**Answer:**
Canny is an edge detection algorithm used to identify boundaries or sharp intensity changes in an image.

---

## 15. What do `50` and `150` mean in Canny?

```python
cv2.Canny(blur, 50, 150)
```

**Answer:**

```text
50  → Lower threshold
150 → Upper threshold
```

They are used by Canny to determine weak and strong edges.

---

## 16. What happens if the Canny thresholds are changed?

**Answer:**
Changing the thresholds changes how many edges are detected. Lower thresholds may detect more edges, including noise, while higher thresholds may detect fewer edges.

---

## 17. What does `cv2.imwrite()` do?

**Answer:**
It saves an image to a file.

---

## 18. Why do you use `output_edges.jpg`?

**Answer:**
It is the required output filename for saving the Canny edge-detected image.

---

## 19. What does `cv2.imshow()` do?

**Answer:**
It displays an image in an OpenCV window.

---

## 20. Why do you use two `imshow()` functions?

**Answer:**
One displays the original image and the other displays the edge-detected image so they can be compared.

---

## 21. What does `cv2.waitKey(0)` do?

**Answer:**
It waits indefinitely until the user presses a key.

---

## 22. What does `cv2.destroyAllWindows()` do?

**Answer:**
It closes all OpenCV display windows.

---

## 23. What happens if `waitKey(0)` is not used?

**Answer:**
The display window may close immediately because the program will continue execution.

---

## 24. What happens if the image path is wrong?

**Answer:**
`cv2.imread()` may return `None`, and later image-processing operations can fail.

---

## 25. How would you check whether the image was loaded successfully?

**Answer:**

```python
if image is None:
    print("Image not found")
```

---

## 26. What is the complete image-processing pipeline?

**Answer:**

```text
Read Image
    ↓
Resize
    ↓
Grayscale
    ↓
Gaussian Blur
    ↓
Canny Edge Detection
    ↓
Save Result
    ↓
Display
```

---

# ⭐ Important Values to Remember

| Value        | Meaning               |
| ------------ | --------------------- |
| `cv2`        | OpenCV Python library |
| `640, 480`   | Width and Height      |
| `BGR2GRAY`   | BGR → Grayscale       |
| `(5, 5)`     | Gaussian kernel size  |
| `0`          | Automatic sigma       |
| `50`         | Canny lower threshold |
| `150`        | Canny upper threshold |
| `waitKey(0)` | Wait indefinitely     |
| `imwrite()`  | Save image            |
| `imshow()`   | Display image         |

---

# ⭐ Most Important Interview Questions

If the interviewer asks quickly, remember these:

### Why grayscale?

**To reduce image complexity and make processing easier.**

### Why Gaussian Blur?

**To reduce noise before edge detection.**

### Why Canny?

**To detect edges and boundaries in an image.**

### Why `(5,5)`?

**It is the Gaussian kernel size.**

### Why `50,150`?

**They are the lower and upper thresholds for Canny Edge Detection.**

### Why `waitKey(0)`?

**To keep the image window open until a key is pressed.**

```
```
