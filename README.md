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








