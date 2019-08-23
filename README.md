# Dataset-Augmentation
basic image augmentation for the limited sized datasets

create folder with name "data". Also create another folder name with "dataset" ==>  "./data/dataset"
copy your images inside dataset folder.

function name =  shift_images(y)
y is the pixel value here. For example when you run shift_images(20),it will shift images to all directions 20 pixels and will mirror and paste on empty black part from original image. At the end, in the same directry of dataset file, there will 4 extra folder:

paste_right
paste_left
paste_up
paste_down

you can expand your dataset for deeplearning applications with this basic augmentation.


height and weight of the image should be equal. i.e: 256 x 256 


