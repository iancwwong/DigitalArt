#!/usr/bin/python

# COMP9517 16s2 Assignment 1: Digital Art
# This program is designed to achieve the following tasks:
#	- Open and read image files
#	- Perform simple mathematical operations on images
#	- Perform filtering using convolution masks
#	- Perform image manipulation and adjustment
# Written by: Ian Wong
# Date started: 7/8/2016

# -------------------------
# IMPORTS
# -------------------------
import sys
import cv2

# -------------------------
# FUNCTIONS
# -------------------------
# Main program
def main(image_filename):

	# Open image file
	img = cv2.imread(image_filename)

	# Convert to greyscale
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	# Output image
	cv2.imwrite(image_filename + "_gray.png", img)
	

# ------------------------------------
if (__name__ == "__main__"):
	if len(sys.argv) < 2:
		print "Usage: python artistic.py <image file>"
		exit()

	main(sys.argv[1])
