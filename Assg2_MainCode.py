"""
Assignment 2 of IPR. This program takes in a single photo,
then based on the function the user chooses
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
import EdgeDetectionBack
import FourierTransformBack
import ImgFilteringBack


global selected_img
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
    
def handle_edge_detection_request():
    """
    """
    # Pass the selected image to back_end:
    EdgeDetectionBack.edge_detection(selected_img)
    

def handle_fourier_transform():
    FourierTransformBack.fourier_transform(selected_img)

def handle_image_filter():
    ImgFilteringBack.Gaussian_noise_filtering(selected_img)

"""Code for running the UI.
    
    This method contains the codes to plot the UI, the color,
    the size of UI and button and displaying the UI.
    
"""    
# Initialize GUI settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main window with size and title
app = customtkinter.CTk()
app.geometry("860x480")
app.title("IPR_Assignment 2")
    
# Button for each action
# Button to selecting image:
detecting_edge_button = customtkinter.CTkButton(master=app, text="Select image", command=handle_path_input)
detecting_edge_button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
    
# Button to detecting edge:
detecting_edge_button = customtkinter.CTkButton(master=app, text="Detecting edge", command=handle_edge_detection_request)
detecting_edge_button.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

detecting_edge_button = customtkinter.CTkButton(master=app, text="Fourier Transform", command=handle_fourier_transform)
detecting_edge_button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

detecting_edge_button = customtkinter.CTkButton(master=app, text="Filter noise", command=handle_image_filter)
detecting_edge_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


    
# Code to start the app:
app.mainloop()
     


    
    
    
    
    
    

    
    
    
       
    