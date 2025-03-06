import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io as io
import skimage as sk

def invert (input_im):
    im_inv=sk.util.invert(input_im, signed_float=True)
    return im_inv

def plot_two_imgs(img1, img2, title1="img1", title='img2'):
    plt.subplot(1,2,1)
    plt.imshow(img1)
    plt.title('im_ref')
    ax = plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title('img1')
    ax = plt.axis('off')