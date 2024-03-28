import cv2
import matplotlib.pyplot as plt
import numpy as np


def edge_detection(selected_img):
    """Detects edge from the given image. 
    
    This method takes an image, convert it to greyscale,
    perform Sobel edge detection using CV2 with thresholding,
    and display both the original image 
    and the image with only the edge detected. 
    
    Args: 
        selected_img: An image path (string)
        
    Returns:
        None. Both images are displayed. 
    """
    
    # Performing greyscale converison:
    img = cv2.imread(selected_img)
    greyscaled_selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Edge detection with Sobel operator (specify x and y directions)
    sobel_x = cv2.Sobel(greyscaled_selected_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(greyscaled_selected_img, cv2.CV_64F, 0, 1, ksize=3)

    # Combine gradients using L2 Norm (optional)
    sobel = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize Sobel output (optional)
    # sobel = np.uint8(255 * sobel / np.max(sobel))

    # Apply thresholding (adjust threshold value as needed)
    thresh = 0.05 * np.max(sobel)
    edge_detected_img = np.where(sobel > thresh, 255, 0).astype(np.uint8)
    
    # Create the figure with subplots
    rows = 1
    column = 2
    sobel_figure = plt.figure(figsize=(20, 10))

    # Displaying original image in the left:
    sobel_figure.add_subplot(rows,column,1)
    plt.imshow(greyscaled_selected_img, cmap="gray")
    plt.title("Original Image")

    # Displaying edge detected image in the left:
    sobel_figure.add_subplot(rows,column,2)
    plt.imshow(edge_detected_img, cmap="gray")
    plt.title("Selected Image, after Sobel edge detection with Thresholding")

    # Adjust layout for better visualization and show both images:
    plt.tight_layout()  
    plt.show()
