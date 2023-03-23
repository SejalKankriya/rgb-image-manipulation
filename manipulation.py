import cv2
import numpy as np

# Reading the original image
org_img = cv2.imread('cvip.jpg', cv2.IMREAD_COLOR)

# Gray scaling an image

grayscale_wt = [0.299, 0.587, 0.114]
original_img_array = org_img[..., :3]
mat = np.dot(original_img_array, grayscale_wt)
grayscale_img = mat.astype(np.uint8)

cv2.imwrite('gray_image.png', grayscale_img)

# Storing the height and weight of the grayscale image
height, width = grayscale_img.shape[:2]

# Storing half-size of the image
new_width = width // 2
new_height = height // 2

# Scaling the gray-scale image

scaled_img = np.zeros((new_height, new_width), dtype=np.uint8)
mean_ht = height / new_height
mean_wt = width / new_width

for i in range(new_height):
    for j in range(new_width):
        scaled_img[i, j] = grayscale_img[int(i * mean_ht), int(j * mean_wt)]
        
cv2.imwrite('gray_image_scaled.png', scaled_img)

# Translating the gray-scale image

translated_img = np.zeros((height, width), dtype=np.uint8)
translated_img[50:, 50:] = grayscale_img[:-50, :-50]

cv2.imwrite('gray_image_translated.png', translated_img)

# Flipping the gray-scale image along the horizontal axis

horizontal_flip = np.flipud(grayscale_img)
cv2.imwrite('gray_image_flip_horizontal.png', horizontal_flip)

# Flipping the gray-scale image along the vertical axis

vertical_flip = np.fliplr(grayscale_img)
cv2.imwrite('gray_image_flip_vertical.png', vertical_flip)

# Invert gray-scale image

inverted_img = 255 - grayscale_img
cv2.imwrite('gray_image_inversion.png', inverted_img)

# Rotating the gray-scale image

# Computing the rotation matrix
degree = np.radians(45)
rot_matrix = np.array([[np.cos(degree), -np.sin(degree)], [np.sin(degree), np.cos(degree)]])

# Computing the rotated image
rotated_img = np.zeros((height, width), dtype=np.uint8)
dim_array = np.array([new_height, new_width])

# Calculating the new image coordinates using rotation matrix
for i in range(height):
    for j in range(width):
        v_center = np.array([i - new_height, j - new_width])
        x, y = np.dot(rot_matrix, v_center) + dim_array
        
        if (x >= 0 and y >= 0 and x < height and y < width):
            rotated_img[i, j] = grayscale_img[int(x), int(y)]

cv2.imwrite('gray_image_rotated.png', rotated_img)

# Save the original image

cv2.imwrite('image.png', org_img)

# BONUS

# Storing and computing mean of the height and weight of the RGB image
rgb_height, rgb_width, channel = org_img.shape

# Storing half-size of the image
new_rgb_width = rgb_width // 2
new_rgb_height = rgb_height // 2

mean_rgb_ht = rgb_height / new_rgb_height
mean_rgb_wt = rgb_width / new_rgb_width

# Scaling the RGB image

scaled_rgb_img = np.zeros((new_rgb_height, new_rgb_width, channel), dtype=np.uint8)

for i in range(128):
    for j in range(256):
        scaled_rgb_img[i, j] = org_img[int(i * 2), int(j * 2)]
        
cv2.imwrite('image_scaled.png', scaled_rgb_img)

# Translating the RGB image

translated_rgb_img = np.zeros((org_img.shape), dtype=np.uint8)
translated_rgb_img[50:, 50:] = org_img[:-50, :-50]

cv2.imwrite('image_translated.png', translated_rgb_img)

# Flipping the RGB image along the horizontal axis

horizontal_rgb_flip = np.flipud(org_img)
cv2.imwrite('image_flip_horizontal.png', horizontal_rgb_flip)

# Flipping the RGB image along the vertical axis

vertical_rgb_flip = np.fliplr(org_img)
cv2.imwrite('image_flip_vertical.png', vertical_rgb_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()