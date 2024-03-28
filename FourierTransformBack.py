import tkinter
import customtkinter
from tkinter import messagebox
import cv2
import matplotlib.pyplot as plt
import numpy as np

def fourier_transform(selected_img):
    """Peform Fourier transform on an image. 
    
    This method takes an image, convert it to greyscale,
    perform Fourier transformation on the image
    and return both the original image 
    and the frequency specturm of the image. 
    
    Args: 
        greyscaled_selected_img: An image, selected by the handle_path_input function
        
    Returns:
        None. Both images are displayed in lieu of return. 
    """
    # Performing greyscale converison:
    img = cv2.imread(selected_img)
    greyscaled_selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Complete the Fourier Transform on the given image:
    fourier_transform = cv2.dft(np.float32(greyscaled_selected_img), flags=cv2.DFT_COMPLEX_OUTPUT)
    
    # Shift the zero-frequency component to the center of the spectrum
    fourier_shift = np.fft.fftshift(fourier_transform)
    
    #
    magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1]))
    
    # Convert the magnitude into display-able image:
    normal_magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    
    # Create the figure with subplots
    rows = 1
    column = 2
    fourier_figure = plt.figure(figsize=(20, 10))
    
    # Displaying original image in the left:
    fourier_figure.add_subplot(rows,column,1)
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    
    # Displaying edge detected image in the left:
    fourier_figure.add_subplot(rows,column,2)
    plt.imshow(normal_magnitude)
    plt.title("Selected Image, after Sobel edge detection")
    
    # Adjust layout for better visualization and show both images:
    plt.tight_layout()  
    plt.show()
