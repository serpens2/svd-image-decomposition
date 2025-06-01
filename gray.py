from svd_custom import SVD
import numpy as np
import cv2

IMAGE_NAME = 'gray_snakes.jpg'
###
img = cv2.imread(IMAGE_NAME,cv2.IMREAD_GRAYSCALE).astype('float')
U,Sigma,V = SVD(img)

'''
For each k in k_arr we consider approximation of the original image
given by the first k singular values (see svd_custom)
'''
SV_num = Sigma.shape[0]
print(f'number of singular values: {SV_num}')
SV_percents = [1,5,10,20,25,50,75]
k_arr = [ int( (percent/100)*SV_num ) for percent in SV_percents ]
for k in k_arr:
    if k != 0: # when SV_num is small, we may get fraction which rounds to 0
        reconst_img = np.zeros_like(img)
        for i in range(k):
            reconst_img += Sigma[i] * np.outer(U[i], V[i])
        # Normalizing image and saving it
        min_ = np.min(reconst_img)
        max_ = np.max(reconst_img)
        normalized_img = (reconst_img - min_)/max_
        img_0_255 = (normalized_img * 255).astype(np.uint8) 
        fname = IMAGE_NAME.split('.')[0] + '_k=' + str(k)+ '.' + IMAGE_NAME.split('.')[1]
        cv2.imwrite(fname,img_0_255)
print('Done')
