# Striatum Cropper

## Functional domains in mouse striatum

In their seminal study, Hintiryan et al. (2016) investigated the functional diversity of the mouse dorsal striatum. 
They developed a detailed connectivity projection map from the cerebral cortex to the dorsal striatum (CP), 
identifying 29 distinct functional striatal domains in three striatal divisions: rostral, intermediate and caudal (Figure 1).

![Screen Shot 2022-06-01 at 6 52 43 PM](https://user-images.githubusercontent.com/19292138/171459024-5bc51455-8835-44ea-98fe-f1c325eecfd8.png)
Figure 1. 29 distinct functional striatal domains

They used three rostral divisions as follows: rostral (Bregma +1.345 mm), intermediate (+0.145 mm), and caudal (-0.655 mm). 
Motivated by the findings of this study, the current project offers an algorithm for automated quantification of functional 
domains in rodent striatum.

## Maximum intensity projection 

3D Z-stacks of the striatum are initially converted the to 2D maximal intensity projection (MIP). MIP creates an output image 
each of whose pixels contains the maximum value over all images in the stack at the particular pixel location (max_inten_proj.py). 
Accordingly, at each pixel position, the pixel with the maximum intensity is found, which become the intensity of that pixel value 
in the projected image. This results in a 2D projection of the original 3D Z-stacks.

## Automated striatum cropping

Following Hintiryan et al.’s paper, coronal brain section images containing three striatal divisions are selected: 
rostral (Bregma +1.345 mm), intermediate (+0.145 mm), and caudal (-0.655 mm). Figure 2 illustrates examples of coronal 
brain images containing the three striatal divisions. The images are initially fed to the algorithm. Based on the pre-defined 
coordinate ratios in each brain section (rostral, intermediate and caudal), the algorithm is able to detect the striatum 
boundaries and crop the left and right striatum as our regions of interest (ROIs) and a part of corpus callosum for 
subsequent analyses. The following provides a description of how the algorithm detect the striatum boundaries in each 
brain section image.

![Screen Shot 2022-06-01 at 6 57 41 PM](https://user-images.githubusercontent.com/19292138/171459537-b19e179c-5c06-4407-a480-a95b9d4dbca6.png)

In the case of intermediate striatum, for instance, the Coronal Level 53 (Bregma +0.145) image from Allen Brain Atlas is selected 
as the model image for intermediate striatum. Using the crop bounding box, the image is cropped in such a way that the whole section 
is bound by the image boundaries (Figure 3).

![Screen Shot 2022-06-01 at 6 58 38 PM](https://user-images.githubusercontent.com/19292138/171459722-4b2ceebb-9a10-4df9-84d4-7cede48054f5.png)

The image is then read using OpenCV (an optimized computer vision library in Python). Several points on the striatum boundaries are 
selected and their coordinates (in height and width) are recorded (Figure 4). The height and width coordinates of each point are then 
divided by the height and width of the entire image, respectively. The resulting coordinate ratios have been stored in a Python file 
named parameters.py. The same procedure is repeated for rostral and caudal striatum images. Using these defined coordinate ratios, 
the algorithm can reliably detect and crop the striatum boundaries in test images, provided that the selected brain image has almost 
the same distance to bregma as the model image. The more similar the selected image to the model image, the more reliable the detection
of striatum boundaries. Figure 5 shows en example of striatum cropping.

![Screen Shot 2022-06-01 at 7 00 04 PM](https://user-images.githubusercontent.com/19292138/171459973-750674b2-97c4-4e1f-9be9-0c7dd5ceea77.png)


![Screen Shot 2022-06-01 at 7 02 21 PM](https://user-images.githubusercontent.com/19292138/171460351-ac6e67df-8271-446e-93d6-1b2aa9e4bd8e.png)

### Tilted brain images

Often times the brain section images are tilted, depending on how the sections are mounted on the objective slide and how the sections 
are imaged (Figure 1). In order to obtain accurate detection of striatum boundary, the axis of symmetry of brain images has to form a 
90-degree angle with the horizontal line of image boundary. Thus, tilted images need to be rotated so that the desired 90-degree angle 
is formed. A separate Python module named rotation.py has been developed to overcome the problem of tilted images. By feeding a tilted 
image into the module, the image is shown to the user along with a vertical line representing the ideal axis of symmetry. The user can 
then mark three points on the image to determine the degree to which the image is tilted.

![Screen Shot 2022-06-01 at 7 04 01 PM](https://user-images.githubusercontent.com/19292138/171460761-3357559f-6c15-4069-a966-aaa1294ebb62.png)

![Screen Shot 2022-06-01 at 7 05 25 PM](https://user-images.githubusercontent.com/19292138/171460967-bade29be-258b-49e1-b7b5-e14b9b844ad0.png)
![Screen Shot 2022-06-01 at 7 05 54 PM](https://user-images.githubusercontent.com/19292138/171460991-5fe37db3-44b8-46dd-b4b2-5ba57872c090.png)

The first point has to be on the spot where the the axis of symmetry of the tilted image cross the ideal vertical line. The second point 
should be placed somewhere above the axis of symmetry and the third one on the vertical line across from the second points. Once the third 
point has been placed, the degree to which the image is tilted is shown. Upon determining the degree of axial tilt of the image, the 
algorithm rotates the image as the degree of axial tilt in the opposite direction, so that its axis of symmetry matches the desired vertical 
line. The tilt-corrected image is then saved in a path specified by the user. Before feeding the tilt-corrected image to the main algorithm, 
the user is required to crop the image in such a way that the whole brain section is bound by the image boundaries.

![Screen Shot 2022-06-01 at 7 08 15 PM](https://user-images.githubusercontent.com/19292138/171461581-7d1a303b-0681-49dd-a0c8-5cb9aaebb569.png)

## Specification of striatal domain boundaries

The tilt-corrected brain images are fed to the algorithm. The algorithm then crops left and right striatum, and a part of corpus callosum in 
each image (i.e., rostral, intermediate and caudal images). Similar to the procedure of striatum boundary detection described earlier, the 
algorithm is able to detect distinct striatal domains (Figure 1) within each striatum image based on pre-defined coordinate ratios. Such 
coordinate ratios are obtained by loading images of cropped striatum (rostral, intermediate and caudal) with specified domain boundaries 
using OpenCV. In each cropped image, boundary points of striatal domains are selected (blue dots in Figure 9) and their coordinates 
(in height and width) are recorded. The height and width coordinates of each point are then divided by the height and width of the entire 
image, respectively. The resulting coordinate ratios have been stored in a Python file named parameters.py. Using these defined coordinate 
ratios, the algorithm can reliably detect and crop distinct striatal domains in striatum images which have been already cropped by the 
algorithm. Figure 10 compares the striatal domains specified by Hintiryan et al. (2016) and the striatal domains detected by the algorithm. 
As observed the algorithm has efficiently detected the distinct striatal domains. Subsequently, the cropped striatal domains are used for 
fiber intensity analysis.

![Screen Shot 2022-06-01 at 7 10 17 PM](https://user-images.githubusercontent.com/19292138/171462087-e4a187eb-befd-4080-8cc8-8164eeaa83c6.png)

![Screen Shot 2022-06-01 at 7 11 15 PM](https://user-images.githubusercontent.com/19292138/171462316-bd05fc26-b00d-4751-97c4-032250dd0446.png)

## Fiber intensity analysis

Once the left and right striatum and corpus callosum have been cropped, and striatal domains have been identified and cropped, the algorithm 
proceeds with TH fiber intensity analysis within each striatal domain. The following provides a description of fiber intensity analysis.
It has to be noted that the algorithm assumes that the left hemisphere (mouse point of view) is the “injected hemisphere". If otherwise, 
the user can flip the image before feeding the image into the algorithm.
For noise calculation, the average pixel intensity of corpus callosum is measured and normalized (0-1). The higher the pixel value means 
the brighter the pixel. Since we are concerned with DA terminals in striatum, the darker the pixels means the more TH terminal in that region. 
Since there is no TH terminal present in corpus callosum, any dark pixels can be regard as noise. Therefore, the average pixel intensity of 
corpus callosum is subtracted from 1 to get the noise level in each brain section. The average pixel intensity of non-injected striatum image 
is calculated and subtracted from 1 to get average TH intensity. The resulting value is subtracted from the noise level to achieve the baseline 
TH signal. The average pixel intensity of each and every striatal domain is calculated, subtracted from 1 to get TH intensity and divided by the 
baseline TH signal. Finally, the normalized TH signal for all striatal domains are outputted as a CSV file.










