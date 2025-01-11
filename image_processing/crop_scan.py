'''
@author RIT GDSC.
@brief This is the image processing code that does the following:
Image Capture: Use a camera or sensor to capture images of the crops.
Image Analysis: Implement image processing techniques to identify crop health indicators (e.g., color, size, leaf condition).
Tools: OpenCV, numpy.
'''
import cv2
import numpy as np

def process_crop_image(image_path):
    '''
    @brief this function is where we process the image.
    @param image_path the path of the image file.
    @return the result of whether the crop is healthy or not.
    '''
    # Load image from file
    np_img = np.fromfile(image_file, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Example processing: Convert to grayscale and find mean intensity (not real health analysis)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean_intensity = np.mean(gray_image)

    # Mock logic for crop health evaluation based on mean intensity
    return "Healthy" if mean_intensity > 127 else "Unhealthy"