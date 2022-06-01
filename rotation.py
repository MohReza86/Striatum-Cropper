''' @author: Mohammadreza Baghery '''

''' This modules allows the user to specify the degree to which the image has tilted. 
The algorithm rotates the image to produce a tilt-free image 

By running the algorithm the image is shown to the user along with a vertical line 
representing the ideal axis of symmetry. The user can then mark three points on the image 
to determine the degree to which the image is tilted

Once the three points have been marked, the user can pres the ESCAPE button to close
the window.
'''

import cv2
import math 
from matplotlib import pyplot as plt 
from scipy import ndimage
from skimage.color import rgb2gray, rgba2rgb, label2rgb


input_path = '' # specify the input image path
output_path = ''   # specify the folder to which the tilt-corrected image is to be saved


img = cv2.imread(input_path)
image_gray = rgb2gray(img)

height, width = image_gray.shape

img = cv2.line(image_gray, (int(width/2), 0), (int(width/2), height), (0, 255, 0), 2)

points_list = [ ]

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x,y)

        size = len(points_list)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(points_list[round((size-1)/3)*3]), (x,y), (0,0,255),2)


        cv2.circle(img, (x,y), 5 ,(0,0,255), cv2.FILLED)
        points_list.append([x,y])
        print(points_list)


def gradient(pt1, pt2):
    return (pt2[1]-pt1[1])/((pt2[0]-pt1[0])+0.1)


def getAngle(points_list):

    global angD
    pt1, pt2, pt3 = points_list[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(img, str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_COMPLEX,
    1.5, (0,0,255),2)
     

while True:
    if len(points_list) == 3:
        getAngle(points_list)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        points_list = []
        img = cv2.imread(input_path)
        image_gray = rgb2gray(img)
        img = cv2.line(image_gray, (int(width/2), 0), (int(width/2), height), (0, 255, 0), 2)

    # Press Esc if you want to end the loop
    elif cv2.waitKey(2) & 0xFF == 27:
        cv2.destroyAllWindows()
        break


img = cv2.imread(input_path)
rotated = ndimage.rotate(img, angD*(-1))
plt.imsave(f'{output_path}/tilt_corrected.tiff',rotated)

        


    


