# RGB Image Manipulation

This program allows you to manipulate a given 512x256 RGB image by performing various operations and outputting resultant images. The following operations can be conducted:

Gray scaling an image: The original RGB image is converted to grayscale and saved as gray_image.png.
Scaling the gray-scale image along both horizontal and vertical axes: The gray-scale image is scaled down to 256x128 and saved as gray_image_scaled.png .
Translating the gray-scale image along both horizontal and vertical axes: The gray-scale image is translated by 50 pixels to the right and 50 pixels to the bottom, and saved as gray_image_translated.png.
Flipping the gray-scale image along the horizontal axis: The gray-scale image is flipped along the horizontal axis passing through the center of the image and saved as gray_image_flip_horizontal.png.
Flipping the gray-scale image along both horizontal and vertical axes: The gray-scale image is flipped along the vertical axis passing through the center of the image and saved as gray_image_flip_vertical.png.
Inverting the gray-scale image: The gray-scale image is inverted by subtracting the gray value from 255 or 1, and saved as gray_image_inversion.png.
Rotating the gray-scale image: The gray-scale image is rotated by 45 degrees in the clockwise direction and saved as gray_image_rotated.png.
Additionally, the original RGB image is saved as image.png.

### Technologies Used

This program is implemented using Python and various image processing libraries, including cv2 and NumPy.All the manipulations of the image are manually coded in python.

### Usage

To use this program, download a 512x256 RGB image (the repository already has one) from the internet, save it as "cvip.jpg" and place it in the same directory as the program file. Then, run the program and it will conduct the above operations and output the resultant images.
