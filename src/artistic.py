#!/usr/bin/python

# -- COMP9517 16s2 Assignment 1: Digital Art
# This program produces an "oil paint" effect on images. To do this,
# it does 3 operations sequentially:
#	1. Pixel-by-pixel mathematical operation
#	2. Convolution mask for most frequent pixel value
#	3. Average intensities of pixels
#
# Written by: Ian Wong
# Date started: 7/8/2016

# -------------------------
# IMPORTS
# -------------------------
import cv2		# image processing
import numpy as np	# scientific math computation
import sys
import os

# -------------------------
# CONSTANTS
# -------------------------

# Index of pixel values
IMG_PIXEL_BLUE = 0
IMG_PIXEL_GREEN = 1
IMG_PIXEL_RED = 2

# -------------------------
# FUNCTIONS
# -------------------------
# Main program
def main(image_filename):

	# Open image file
	img = cv2.imread(image_filename)	# img is of type "numpy.ndarray"

	# Conduct task 1
	task1_img = task1(img)
	cv2.imwrite("_task1.png", task1_img)

	# Conduct task 2
	task2_img = task2(task1_img)
	cv2.imwrite("_task2.png",task2_img)

	# Conduct task 3
#	task3_img = task3(task2_img)
#	cv2.imwrite("_task3.png", task3_img)

	# Additional effect - Gaussian Blur
#	blurred = gaussian_blur(task3_img)
#	cv2.imwrite("_opt.png", blurred)

# Convert an image to greyscale
def conv_greyscale(img):
	return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Blur an image using the gaussian kernel
def gaussian_blur(img):
	print "Blurring image using Gaussian Kernel..."
	return cv2.GaussianBlur(img, (5,5), 0)		# (5,5) is size of kernel; 0 is std_dev of x and y

# Task 1: Changes each pixel using the formula:
#	I = 0.299r + 0.587g + 0.114b
def task1(img):
	print "Conducting task 1..."
	proc_img = img.copy()
	
	# obtain dimensions of image
	height, width, depth = img.shape
	for i in range(0, height):
		for j in range(0, width):

			# Obtain pixel RGB values
			r = img.item(i,j,IMG_PIXEL_RED)
			g = img.item(i,j,IMG_PIXEL_GREEN)	
			b = img.item(i,j,IMG_PIXEL_BLUE)

			# Set new pixel value
			new_pixel_val = 0.299*r + 0.587*g + 0.114*b
			proc_img.itemset((i,j,0),new_pixel_val)			# optimised access method
			proc_img.itemset((i,j,1),new_pixel_val)
			proc_img.itemset((i,j,2),new_pixel_val)

	return proc_img

# Task 2: Application of a convolution mask that determines 
#	  the most frequent pixel value
def task2(img):
	print "Conducting task 2..."
	proc_img = img.copy()

	# Obtain dimensions of image
	height, width, depth = img.shape
	for i in range(0, height):
		for j in range(0, width):
			# Get value of pixel (at i,j) and its neighbours
			neighbour_vals = get_neighbours(img, (3,3), (i,j))	# 3x3 mask
			
			# Get most frequent pixel value
			most_freq_val = get_most_freq_val(neighbour_vals)
	
			# Set pixel value to be most frequent pixel value
			proc_img.itemset((i,j,0),most_freq_val)
			proc_img.itemset((i,j,1),most_freq_val)
			proc_img.itemset((i,j,2),most_freq_val)

	return proc_img

# Obtains the neighbouring pixel values as an array
# NOTE: Assumes mask dimensions are odd, pixel_loc is valid, and img is a GREYSCALE image
def get_neighbours(img, mask_dim, pixel_loc):
	neighbours = []

	# Obtain necessary dimensions
	mask_height, mask_width = mask_dim
	img_height, img_width, img_depth = img.shape
	pixel_x, pixel_y = pixel_loc
	
	# Iterate over mask region, with pixel at centre of mask
	for i in range(pixel_x - mask_height/2, pixel_x + mask_height/2 + 1):
		if (i >= 0) and (i < img_height):			# check for height bounded
			for j in range(pixel_y - mask_width/2, pixel_y + mask_width/2 + 1):
				if (j >= 0) and (j < img_width):	# check for width bounded
					neighbours.append(img.item(i,j,0))
			
	return neighbours
	

# Obtains the most frequent value in an array
def get_most_freq_val(values):
	return np.bincount(values).argmax()

# Task 3: Achieves the 'oil paint' effect
def task3(img):
	print "Conducting task 3..."
	proc_img = img.copy()

	# Do some processing

	return proc_img

# -----------------------------------------------------------------------------------
if (__name__ == "__main__"):

	# Check correct program usage
	if len(sys.argv) < 2:
		print "Usage: python artistic.py <image file>"
		exit()

	# Check image file exists
	elif not os.path.exists(sys.argv[1]):
		print "Error: File '" + sys.argv[1] + "' not found."
		exit()

	main(sys.argv[1])
