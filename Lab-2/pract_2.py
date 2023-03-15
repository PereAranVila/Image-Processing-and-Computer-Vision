
from skimage import data
import matplotlib.pyplot as plt
import numpy as np


im = data.retina()

# original picture

plt.figure()
plt.axis('off')
plt.title('Original picture')
plt.imshow(im)
plt.savefig('original-img-retina.png')
plt.show()

###############################################################################
# Channel extraction

print("Size of the image: ", im.shape)
print("The image is with 8 bits")

# gray scale 
im_grisos = np.copy(im)
R = im_grisos[:, :, 0]
G = im_grisos[:, :, 1]
B = im_grisos[:, :, 2]


# RGB images only with red, green and blue channels
red_channel = np.copy(im)
red_channel[:, :, 1] = 0
red_channel[:, :, 2] = 0
green_channel = np.copy(im)
green_channel[:, :, 0] = 0
green_channel[:, :, 2] = 0
blue_channel = np.copy(im)
blue_channel[:, :, 0] = 0
blue_channel[:, :, 1] = 0


# plot gray images 
plt.figure()
plt.subplot(2,3,1)
plt.axis('off')
plt.imshow(R, cmap = 'gray')
plt.subplot(2,3,2)
plt.axis('off')
plt.imshow(G, cmap ='gray')
plt.subplot(2,3,3)
plt.axis('off')
plt.imshow(B, cmap = 'gray')

# plot RGB images with only red, green and blue channels each
plt.subplot(2,3,4)
plt.axis('off')
plt.imshow(red_channel)
plt.subplot(2,3,5)
plt.axis('off')
plt.imshow(green_channel)
plt.subplot(2,3,6)
plt.axis('off')
plt.imshow(blue_channel)
plt.savefig('all-channels-and-R-G-B-retina.png')
plt.show()

###############################################################################
# Luminacence, Colormaps, False Color and Gamma Contrast'

# values need o be double to do operations
R = R/255.
G = G/255.
B = B/255.

# Average of the 3 channels and plot
M = 0.3333*(R+G+B)
plt.figure()
plt.title('Average RGB')
plt.axis('off')
plt.imshow(M, cmap='gray')   #from 0 to 1
plt.savefig('average-channels-retina.png')
plt.show()

# Luminance of the original color image
L = 0.299*R + 0.587*G + 0.114*B
plt.figure()
plt.title('Luminance')
plt.axis('off')
plt.imshow(L, cmap='gray')       #from 0 to 1
plt.savefig('luminance-retinda.png')
plt.show()

# display the luminance with different colormaps
plt.figure()
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Luminance cmap viridis') 
plt.imshow(L, cmap = 'viridis')
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Luminance cmap jet')
plt.imshow(L, cmap = 'jet')
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Luminance cmap rainbow')
plt.imshow(L, cmap = 'rainbow')
plt.subplot(2,2,4)
plt.title('Luminance cmap Purples')
plt.axis('off')
plt.imshow(L, cmap ='Purples')
plt.savefig('luminance-colormaps-retina.png')
plt.show()

# Gamma contrast 0<g<1
g = 0.70
immg_0 = np.copy(im)
# Resize 0-255 int to 0-1 doble
immg_0 = immg_0**g /255.
immg_0 = immg_0 / immg_0.max()

plt.figure()
plt.title('gamma contrast g=0.70')
plt.axis('off')
plt.imshow(immg_0)
plt.savefig('gamma-contrast-1.png')
plt.show()

# Gamma contrast g>1
g = 1.2
immg_1 = np.copy(im)
# resize 0-255 int to 0-1 doble
immg_1 = immg_1**g /255.
immg_1 = immg_1 / immg_1.max()

plt.figure()
plt.title('gamma contrast g=1.2')
plt.axis('off')
plt.imshow(immg_1)
plt.savefig('gamma-contrast-2.png')
plt.show()