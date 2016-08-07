#!/usr/bin/python

# -- COMP9517 16s2 Assignment 1: Digital Art
# This program produces an "oil paint" effect on images. To do this,
# it does 3 tasks sequentially:
#	1. pixel-by-pixel mathematical operation
#	2. convolution mask for most frequent pixel value
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

	# Conduct task 2
	task2_img = task2(task1_img)
	output_filename = os.path.splitext(image_filename)[0] + "_task2.png"
	cv2.imwrite(output_filename, task1_img)	

	# Output final image
	outputfilename = os.path.splitext(image_filename)[0] + "_oiled.png"
	cv2.imwrite(output_filename, task3_img)

# Convert an image to greyscale
def conv_greyscale(img):
	return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Task 1: Changes each pixel using the formula:
#	I = 0.299r + 0.587g + 0.114b
def task1(img):
	proc_img = img.copy()
	
	# obtain dimensions of image
	height, width, depth = img.shape
	img = np.reshape(img, (height,width,depth))	# convert to array for fast iteration
	for i in range(0,height):
		for j in range(0,width):

			# Obtain pixel RGB values
			r = img[i][j][IMG_PIXEL_RED]
			g = img[i][j][IMG_PIXEL_GREEN]
			b = img[i][j][IMG_PIXEL_BLUE]

			proc_img[i][j] = 0.299*r + 0.587*g + 0.114*b

	# DEBUGGING - output image
	cv2.imwrite("_task1.png", proc_img)

	return proc_img

# Task 2: Application of a convolution mask that determines 
#	  the most frequent pixel value
def task2(img):
	proc_img = img.copy()

	# Do some processing

	# DEBUGGING - output image
	cv2.imwrite("_task2.png",proc_img)

	return proc_img

# Task 3: Achieves the 'oil paint' effect
def task3(img):
	proc_img = img.copy()

	# Do some processing

	# DEBUGGING - output image
	cv2.imwrite("_task3.png",proc_img)

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
