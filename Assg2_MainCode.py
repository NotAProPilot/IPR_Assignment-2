"""
Assignment 2 of IPR. This program takes in a single photo,
then based on the function the user choose 
(Edge Detection, Histogram Display and Noise Reduction)
the program will display the original photo and the appopirate photo. 
"""

import random
import tkinter
import customtkinter
from tkinter import messagebox
import cv2
import matplotlib.pyplot as plt
import numpy as np

def ui_maker():
    """This method contains necessary code to make an UI.
    
    This method contains the codes to plot the UI, the color,
    the size of UI and button and displaying the UI.
    
    Args: None.
    """
    # Initialize GUI settings
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    # Create the main window with size and title
    app = customtkinter.CTk()
    app.geometry("860x480")
    app.title("IPR_Assignment 2")
    
    
def handle_path_input():
    """Converting selected image to filepath. 
    
    This method prompts the user to select an image file 
    using a file dialog.
    
    Args: None.
    
    Return: A file path that corresponds to the file choosen by the user. 
    
    """
    global selected_img
    selected_img = customtkinter.filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif")]
    )
    
def edge_detection(selected_img):
    """Detects edge from the given image. 
    
    This method takes an image, convert it to greyscale,
    perform Sobel edge detection using CV2,
    and return both the original image 
    and the image with only the edge detected. 
    
    Args: 
        file_path: An image, selected by the handle_path_input function
        
    Returns:
        None. Both images are displayed in lieu of return. 
    """
    
    # Performing greyscale converison:
    greyscaled_selected_img = cv2.cvtColor(selected_img, cv2.COLOR_BGR2GRAY)
    
    # Edge detection for both axis:
    # For best performance, kernel size could be set to 3 or 5
    # Kernel size here are randomly set to any odd number between 3 and 7
    edge_detected_img = cv2.Sobel(src=greyscaled_selected_img,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=random.randrange(3,5,2))
    
    # Create the figure with subplots
    rows = 1
    column = 2
    sobel_figure = plt.figure(figsize=(20, 10))
    
    # Displaying original image in the left:
    sobel_figure.add_subplot(rows,column,1)
    plt.imshow(cv2.cvtColor(selected_img,cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    
    # Displaying edge detected image in the left:
    sobel_figure.add_subplot(rows,column,2)
    plt.imshow(edge_detected_img)
    plt.title("Selected Image, after Sobel edge detection")
    
    # Adjust layout for better visualization and show both images:
    plt.tight_layout()  
    plt.show()

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
    greyscaled_selected_img = cv2.cvtColor(selected_img, cv2.COLOR_BGR2GRAY)
    
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
    plt.imshow(cv2.cvtColor(selected_img,cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    
    # Displaying edge detected image in the left:
    fourier_figure.add_subplot(rows,column,2)
    plt.imshow(normal_magnitude)
    plt.title("Selected Image, after Sobel edge detection")
    
    # Adjust layout for better visualization and show both images:
    plt.tight_layout()  
    plt.show()

def 
    
     
     
    

    
    
    
    
    
    

    
    
    
       
    