#from parameters.py import *
import cv2
from matplotlib import pyplot as plt 
from skimage.color import rgb2gray, rgba2rgb, label2rgb
import numpy as np
import csv


input_path = ''
output_path = ''

animal_No = ''
week_No = ''
str_division = 'CPi'


img = cv2.imread(input_path)
image_gray = rgb2gray(img)
height, width = image_gray.shape


def cp_domains(coordin, img):
    ''' The function takes coordinates of the polygon of ineterst
    as an inpit and returns the cropped polygon.
    The function follows the following steps:
    1) find region using the poly points
    2) create mask using the poly points
    3) do mask op to crop
    '''
    pts = np.array(coordin) # creating an array of point coordinates 
    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x,y,w,h = rect
    croped = img[y:y+h, x:x+w].copy()
    # (2) make mask
    pts = pts - pts.min(axis=0)
    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    ## (3) do bit-op
    cropped_mask = cv2.bitwise_and(croped, croped, mask=mask)

    return cropped_mask 


def int_pts_inj(width, height):
    # intermediate striatum (injected hemisphere) coordinates --> left hemisphere (mouse POV)
    int_pts_inj = [[int(width*0.62), int(height*0.28)], [int(width*0.642), int(height*0.27)], [int(width*0.701), int(height*0.282)],
    [int(width*0.758), int(height*0.318)],[int(width*0.813), int(height*0.376)],[int(width*0.844), int(height*0.44)], 
    [int(width*0.864), int(height*0.511)],[int(width*0.859), int(height*0.625)],[int(width*0.848), int(height*0.682)], 
    [int(width*0.831), int(height*0.715)],[int(width*0.769), int(height*0.753)],[int(width*0.712), int(height*0.725)],
    [int(width*0.635), int(height*0.664)],[int(width*0.6), int(height*0.531)],[int(width*0.595), int(height*0.392)]]

    return int_pts_inj

def int_pts_non_inj(width, height):
    # intermediate striatum (non-injected hemisphere) coordinates --> right hemisphere (mouse POV)
    int_pts_non_inj = [[int(width*0.382), int(height*0.285)], [int(width*0.33), int(height*0.275)], [int(width*0.207), int(height*0.351)],
    [int(width*0.15), int(height*0.458)], [int(width*0.13), int(height*0.547)], [int(width*0.144), int(height*0.648)],
    [int(width*0.192), int(height*0.758)], [int(width*0.234), int(height*0.766)], [int(width*0.311), int(height*0.717)],
    [int(width*0.366), int(height*0.656)], [int(width*0.401), int(height*0.537)], [int(width*0.406), int(height*0.392)]]

    return int_pts_non_inj

def int_pts_cc(width, height):
    # corpus collasum coordinates --> right hemisphere (mouse POV)
    int_pts_cc = [[int(width*0.382), int(height*0.27)], [int(width*0.33), int(height*0.26)],
    [int(width*0.3), int(height*0.24)], [int(width*0.38), int(height*0.21)]]

    return int_pts_cc


int_pts_inj = cp_domains(int_pts_inj(width, height), img)
int_pts_inj_gray = rgb2gray(int_pts_inj)
height_inj, width_inj = int_pts_inj_gray.shape

int_pts_non_inj = cp_domains(int_pts_non_inj(width, height), img)
int_pts_non_inj_gray = rgb2gray(int_pts_non_inj)
height_non_inj, width_non_inj = int_pts_non_inj_gray.shape

int_pts_cc = cp_domains(int_pts_cc(width, height), img)
#int_pts_cc_gray = rgb2gray(int_pts_cc)


i_dm_dm = [[0, 0], [0, int(height_inj*0.262)], [int(width_inj*0.148), int(height_inj*0.252)], [int(width_inj*0.105), 0]]
i_dm_d = [[int(width_inj*0.105),0],[int(width_inj*0.148),int(height_inj*0.252)],[int(width_inj*0.176),int(height_inj*0.257)],[int(width_inj*0.251), int(height_inj*0.240)], [int(width_inj*0.329),0]]
i_dm_dl = [[int(width_inj*0.329),0],[int(width_inj*0.251),int(height_inj*0.240)],[int(width_inj*0.383),int(height_inj*0.294)],[int(width_inj*0.649),0]]
i_dl_d = [[int(width_inj*0.649),0],[int(width_inj*0.383),int(height_inj*0.294)],[int(width_inj*0.449),int(height_inj*0.391)],[int(width_inj*0.566),int(height_inj*0.387)],[int(width_inj*0.83),0]]
i_dl_imd = [[int(width_inj*0.83),0],[int(width_inj*0.566),int(height_inj*0.387)],[int(width_inj*0.576),int(height_inj*0.397)],[width_inj, int(height_inj*0.41)]]
i_vl_imv = [[width_inj, int(height_inj*0.41)],[int(width_inj*0.576),int(height_inj*0.397)],[int(width_inj*0.689),int(height_inj*0.614)],[width_inj,int(height_inj*0.458)]]
i_vl_v = [[width_inj,int(height_inj*0.458)],[int(width_inj*0.689),int(height_inj*0.614)],[int(width_inj*0.92),height_inj]]
i_vl_vt = [[int(width_inj*0.92),height_inj],[int(width_inj*0.689),int(height_inj*0.614)],[int(width_inj*0.474),int(height_inj*0.656)],[int(width_inj*0.439),int(height_inj*0.688)],[int(width_inj*0.542),height_inj]]
i_vm_v = [[int(width_inj*0.542),height_inj],[int(width_inj*0.439),int(height_inj*0.688)],[int(width_inj*0.401),int(height_inj*0.683)],[0,int(height_inj*0.804)]]
i_vm_vm = [[0,int(height_inj*0.804)],[int(width_inj*0.401),int(height_inj*0.683)],[int(width_inj*0.186),int(height_inj*0.511)],[0,int(height_inj*0.586)]]
i_dm_im = [[0,int(height_inj*0.586)],[int(width_inj*0.186),int(height_inj*0.511)],[int(width_inj*0.166),int(height_inj*0.257)],[int(width_inj*0.1479),int(height_inj*0.252)],[0,int(height_inj*0.262)]]
i_dm_cd = [[int(width_inj*0.186),int(height_inj*0.511)],[int(width_inj*0.166),int(height_inj*0.257)],[int(width_inj*0.251), int(height_inj*0.240)],[int(width_inj*0.383),int(height_inj*0.294)],[int(width_inj*0.449),int(height_inj*0.391)], [int(width_inj*0.411), int(height_inj*0.434)]]
i_vl_cvl = [[int(width_inj*0.411),int(height_inj*0.434)],[int(width_inj*0.449),int(height_inj*0.391)],[int(width_inj*0.566),int(height_inj*0.387)],
[int(width_inj*0.576),int(height_inj*0.397)],[int(width_inj*0.689),int(height_inj*0.614)],[int(width_inj*0.474),int(height_inj*0.656)]]
i_vm_cvm = [[int(width_inj*0.411),int(height_inj*0.434)],[int(width_inj*0.474),int(height_inj*0.656)],[int(width_inj*0.439),int(height_inj*0.688)],
[int(width_inj*0.401),int(height_inj*0.683)], [int(width_inj*0.186),int(height_inj*0.511)]]


# Cropping the striatal domains in CPi
i_dm_dm = cp_domains(i_dm_dm, int_pts_inj)
i_dm_d = cp_domains(i_dm_d, int_pts_inj)
i_dm_dl = cp_domains(i_dm_dl, int_pts_inj)
i_dl_d = cp_domains(i_dl_d, int_pts_inj)
i_dl_imd = cp_domains(i_dl_imd, int_pts_inj)
i_vl_imv = cp_domains(i_vl_imv, int_pts_inj)
i_vl_v = cp_domains(i_vl_v, int_pts_inj)
i_vl_vt = cp_domains(i_vl_vt, int_pts_inj)
i_vm_v = cp_domains(i_vm_v, int_pts_inj)
i_vm_vm = cp_domains(i_vm_vm, int_pts_inj)
i_dm_im = cp_domains(i_dm_im, int_pts_inj)
i_dm_cd = cp_domains(i_dm_cd, int_pts_inj)
i_vl_cvl = cp_domains(i_vl_cvl, int_pts_inj)
i_vm_cvm = cp_domains(i_vm_cvm, int_pts_inj)


def corp_col(img): 
# Corpus collusom (noise baseline)
    img_corp_col = rgb2gray(img)
    mean_corp_col = img_corp_col[np.nonzero(img_corp_col)].mean() # average of non_zero pixels
    mean_corp_col = 1 - mean_corp_col # gets the noise mean value

    return mean_corp_col

noise = corp_col(int_pts_cc)


def non_inj(img):
    # Non_injected hemisphere intensity 
    mean_non_inj = img[np.nonzero(img)].mean() # average of non_zero pixels
    mean_non_inj = 1 - mean_non_inj # gets the TH mean value

    return mean_non_inj


non_inj_intensity = non_inj(int_pts_non_inj_gray)
baseline_intensity = non_inj_intensity - noise

def inj(domain_img, noise, baseline_intensity): 

    domain_img_gray = rgb2gray(domain_img)
    mean_domain_img = domain_img_gray[np.nonzero(domain_img_gray)].mean() # average of non_zero pixels
    mean_domain_img = 1 - mean_domain_img # gets the TH mean value
    mean_domain_img = mean_domain_img - noise # noise free intensity 
    mean_domain_img_norm = mean_domain_img/baseline_intensity # normalized intensity of each domain

    return mean_domain_img


i_dm_dm_int = inj(i_dm_dm, noise, baseline_intensity)
i_dm_d_int = inj(i_dm_d,  noise, baseline_intensity)
i_dm_dl_int = inj(i_dm_dl,  noise, baseline_intensity)
i_dl_d_int = inj(i_dl_d,  noise, baseline_intensity)
i_dl_imd_int = inj(i_dl_imd,  noise, baseline_intensity)
i_vl_imv_int = inj(i_vl_imv, noise, baseline_intensity)
i_vl_v_int = inj(i_vl_v, noise, baseline_intensity)
i_vl_vt_int = inj(i_vl_vt, noise, baseline_intensity)
i_vm_v_int = inj(i_vm_v, noise, baseline_intensity)
i_vm_vm_int = inj(i_vm_vm, noise, baseline_intensity)
i_dm_im_int = inj(i_dm_im, noise, baseline_intensity)
i_dm_cd_int = inj(i_dm_cd, noise, baseline_intensity)
i_vl_cvl_int = inj(i_vl_cvl, noise, baseline_intensity)
i_vm_cvm_int = inj(i_vm_cvm, noise, baseline_intensity)


data_list = [animal_No, week_No, str_division, i_dm_dm_int, i_dm_d_int, i_dm_dl_int, i_dl_d_int,
i_dl_imd_int, i_vl_imv_int, i_vl_v_int, i_vl_vt_int, i_vm_v_int, i_vm_vm_int, i_dm_im_int,
i_dm_cd_int, i_vl_cvl_int, i_vm_cvm_int]

header = ['Animal_No', 'Week No.', 'Striatal division', 'i_dm_dm', 'i_dm_d', 'i_dm_dl',
'i_dl_d', 'i_dl_imd', 'i_vl_imv', 'i_vl_v', 'i_vl_vt', 'i_vm_v', 'i_vm_vm', 'i_dm_im',
'i_dm_cd', 'i_vl_cvl', 'i_vm_cvm'] 


filename = f"{output_path}/TH_Density_Str_Domains.csv"

with open(filename, 'w') as f:
    wr = csv.writer(f)
    wr.writerow(header)

with open(filename, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data_list)

