''' The module reads all Z-stack (3D) czi format images in a folder and outputs the corresponding     
    maximum intensity projection (MIP) images (2D) in the output folder. It further outputs
    the MIP images for each channel.'''

''' @ author: Mohammadreza Baghery '''

import czifile
import numpy as np
from matplotlib import pyplot as plt 
import os

input_path = ''  # please specify the input folder 
output_path = ''  # please specify the output folder 
output_format = '.tiff'  # output format of the MIP images


def max_inten_proj():

    for image in os.listdir(input_path):
        if 'czi' in str(image): # reads only czi format images
            img = czifile.imread(input_path + '/'+ image)  # reading each image in the folder
            scene, channel, z_stack, height, width, time = img.shape # specifying image information

            if channel == 1:  # in case there is only one channel
                img_arr = img[0, 0, :, :, :, 0] # image array 
                max_intensity = np.max(img_arr, axis=0) # maximum intensity projection (MIP) image on the Z axis
                plt.imsave(output_path + '/'+ image + output_format, max_intensity, cmap = 'gray') # saving the MIP image

            else:             # in case there are two channels
                img_arr_ch1 = img[0, 0, :, :, :, 0] # image array for channel #1
                img_arr_ch2 = img[0, 1, :, :, :, 0] # image array for channel #2
                max_intensity_ch1 = np.max(img_arr_ch1, axis=0) # maximum intensity projection for channel #1
                max_intensity_ch2 = np.max(img_arr_ch2, axis=0) # maximum intensity projection for channel #2
                plt.imsave(output_path + '/'+ image + '_ch1' + output_format, max_intensity_ch1, cmap = 'gray')
                plt.imsave(output_path + '/'+ image + '_ch2' + output_format, max_intensity_ch2, cmap = 'gray')


if __name__ == "__main__":
    max_inten_proj()