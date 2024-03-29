import cv2
from PIL import Image
from util import get_limits
yellow = [0,255,255]
cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit )
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

A bounding box is a rectangular box that represents 
the spatial extent of an object or region within an image.
"""
#print(bbox)


"""
if bbox is not None:: This conditional statement checks whether the bbox variable is not None.
 If bbox is not None, it means that a bounding box has been provided.

x1, y1, x2, y2 = bbox: This line unpacks the values from the bbox tuple into four variables: x1, y1, x2, and y2. These variables represent the coordinates of the top-left corner (x1, y1) and the bottom-right corner (x2, y2) of the bounding box.
we are trying to construct a rectangle around the yellow obj
and it's color should be green as denoted by 0,255,255
its thickeness has to be 5
upperleft corner which is x1,y1
lower right x2,y2
"""

"""
This Python code is for capturing video from the default camera (usually the webcam) using OpenCV. Here's a breakdown:

1. **Importing Library**: 
    - `import cv2`: This imports the OpenCV library.

2. **Capturing Video**: 
    - `cap = cv2.VideoCapture(0)`: This line creates a VideoCapture object, initializing the capture device (webcam) with index 0. This assumes that the webcam is the default capture device. If you have multiple cameras connected, you might need to change the index accordingly.

3. **Video Capture Loop**: 
    - `while True:`: This initiates an infinite loop to continuously capture frames from the video stream.
    - `ret, frame = cap.read()`: This line reads a frame from the video capture object (`cap`). It returns two values - `ret`, a boolean indicating whether the frame was successfully read, and `frame`, the captured frame itself.

4. **Displaying the Frame**: 
    - `cv2.imshow('frame', frame)`: This displays the captured frame in a window named 'frame'. The `imshow()` function takes two arguments - the window name and the frame to be displayed.

5. **Exiting the Loop**: 
    - `if cv2.waitKey(1) & 0xFF == ord('q'):`: This line waits for a key press. If the pressed key is 'q', it breaks out of the loop.
    - `cv2.waitKey(1)` waits for 1 millisecond for a key event.
    - `0xFF` is a hexadecimal constant that is used to mask the key value returned by `waitKey()` to ensure that only the least significant 8 bits of the value are retained, which helps with cross-platform compatibility.
    - `ord('q')` returns the Unicode code point for the character 'q'.

6. **Releasing Resources**: 
    - `cap.release()`: This releases the VideoCapture object, freeing the resources associated with it (in this case, the webcam).
    
7. **Closing OpenCV Windows**: 
    - `cv2.destroyAllWindows()`: This closes all OpenCV windows. It's good practice to call this function after you're done working with OpenCV windows to clean up resources and prevent any unexpected behavior.

This code essentially captures video from the webcam and displays it in a window. Pressing 'q' will close the window and end the program.
"""
