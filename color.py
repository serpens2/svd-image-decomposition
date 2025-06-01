from svd_custom import SVD
import numpy as np
import cv2

IMAGE_NAME = 'color_snake.jpg'
# how many singular values to use in reconstruction, in percents
SV_percent = 25 
### image normalization
def norm_img(A):
    min_ = np.min(A)
    max_ = np.max(A)
    A = (A - min_)/max_
    A = (A * 255).astype(np.uint8)
    return A
###
img = cv2.imread(IMAGE_NAME)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = img.astype('float')

# Decomposing image into red, green and blue channels
img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]

# Performing SVD on each channel
U_red, Sigma_red, V_red = SVD(img_red)
U_green, Sigma_green, V_green = SVD(img_green)
U_blue, Sigma_blue, V_blue = SVD(img_blue)

# Calculating number of singular values to be used
k_red = int( Sigma_red.shape[0] * (SV_percent / 100) )
k_green = int( Sigma_green.shape[0] * (SV_percent / 100) )
k_blue = int( Sigma_blue.shape[0] * (SV_percent / 100) )
k = np.min([k_red, k_green, k_blue])

# Reconstructing each channel separately
reconst_red = np.zeros_like(img_red)
for i in range(k):
    reconst_red += Sigma_red[i] * np.outer(U_red[i], V_red[i])
reconst_green = np.zeros_like(img_green)
for i in range(k):
    reconst_green += Sigma_green[i] * np.outer(U_green[i], V_green[i])
reconst_blue = np.zeros_like(img_blue)
for i in range(k):
    reconst_blue += Sigma_blue[i] * np.outer(U_blue[i], V_blue[i])

# Normalization of each channel
reconst_red = norm_img(reconst_red)
reconst_green = norm_img(reconst_green)
reconst_blue = norm_img(reconst_blue)

# Uniting channels in a single image and saving it
reconst_img = np.stack( (reconst_blue,reconst_green,reconst_red),axis=2 )
fname = IMAGE_NAME.split('.')[0] + '_k=' + str(k) + '.' + IMAGE_NAME.split('.')[1]
cv2.imwrite(fname, reconst_img)
print('Done')
