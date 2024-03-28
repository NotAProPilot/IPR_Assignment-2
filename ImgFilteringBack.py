import random
import tkinter
import customtkinter
from tkinter import messagebox
import cv2
import matplotlib.pyplot as plt
import numpy as np


def Gaussian_noise_filtering(selected_img):
    """Add Gaussian noise and perform Frequency Filtering reduction
    
    This method takes in an image, add Gaussian noise to the image,
    then apply a low pass filter in the frequency domain to
    reduce the noise.
    
     Args: 
        greyscaled_selected_img: An image, selected by the handle_path_input function
    
    
    """
    # Add Gaussian noise to the image
    # Performing greyscale converison:
    img = cv2.imread(selected_img)
    greyscaled_selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Generate Gaussian noise to selected image same shape:
    Gaussian_noise = np.random.normal(0,50,greyscaled_selected_img.shape)
    
    # Add the noise to the image:
    img_with_noise = greyscaled_selected_img + Gaussian_noise
    
    # Clip the pixel values to be between 0 and 255.
    img_with_noise = np.clip(img_with_noise, 0, 255).astype(np.uint8)
    
    
    # Reducing noise using low-pass filter:
    # Generating a 2D matrix for the kernel
    # Kernel size is randomly genereated between 3 and 5
    kernel_size = random.randrange(3,5,2)
    low_pass_kernel = np.ones((kernel_size, kernel_size), np.float32)/30
    
    # Remove noise from the image:
    img_noise_reduced = cv2.filter2D(src=img_with_noise, ddepth=-1, kernel=low_pass_kernel)
    
    # Using plt to plot the original, image with noise and imgae with noise reduced
    rows = 1
    column = 3 
    figure = plt.figure(figsize=(20, 10))

    figure.add_subplot(rows, column, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image (Color)")

    figure.add_subplot(rows, column, 2)
    plt.imshow(img_with_noise)  # Use "gray" colormap for grayscale display
    plt.title("Image with Gaussian noise added")
    
    figure.add_subplot(rows, column, 3)
    plt.imshow(img_noise_reduced)  # Use "gray" colormap for grayscale display
    plt.title("Image after using low pass filter")
    

    plt.tight_layout()  # Adjust layout for better visualization
    plt.show()