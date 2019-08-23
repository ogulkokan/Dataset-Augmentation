#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:03:46 2019

@author: Onur
"""
import os
from PIL import Image
import shutil
import errno
from tqdm import tqdm

"""
shift_images(y)  

y is the pixel value. it is working with all square shaped images i.e (256x256). if you choose y = 30 and run function,
images in dataset will shift all directions 30 pixels and black parts will be mirrored from original image. 
At the end, in the same directry of dataset file, there will 4 extra folder:

paste_right
paste_left
paste_up
paste_down

you can expand your dataset for deeplearning applications with this basic augmentation.

***Put all the images inside dataset folder

"""

#os.chdir('data') #this function is changing direction to data folder
#os.mkdir('anan') #this function is creating a new folder named 'anan' in that direction


path = "data/dataset/"



###will create folders to keep cropped and mirrored images. After end of the process, all other folders will be removed again.


shift_up = os.mkdir('data/shift_up')
os.mkdir('data/crop_mirror_up')

try:
    os.mkdir('data/paste_up/')
except OSError as e:
    if e.errno == errno.EEXIST:
        print('Directory not created.')
    else:
        raise




os.mkdir('data/shift_right')
os.mkdir('data/crop_mirror_right')

try:
    os.mkdir('data/paste_right/')
except OSError as e:
    if e.errno == errno.EEXIST:
        print('Directory not created.')
    else:
        raise


os.mkdir('data/shift_left')
os.mkdir('data/crop_mirror_left')

try:
    os.mkdir('data/paste_left/')
except OSError as e:
    if e.errno == errno.EEXIST:
        print('Directory not created.')
    else:
        raise



os.mkdir('data/shift_down')
os.mkdir('data/crop_mirror_down')



try:
    os.mkdir('data/paste_down/')
except OSError as e:
    if e.errno == errno.EEXIST:
        print('Directory not created.')
    else:
        raise




"""
named created folders to process "up"

"""
shift_up = 'data/shift_up/'
crop_mirror_up = 'data/crop_mirror_up/'
paste_up = 'data/paste_up/'

"""
named created folders to process "right"

"""
shift_right = 'data/shift_right/'
crop_mirror_right = 'data/crop_mirror_right/'
paste_right = 'data/paste_right/'

"""
named created folders to process "left"

"""

shift_left = 'data/shift_left/'
crop_mirror_left = 'data/crop_mirror_left/'
paste_left = 'data/paste_left/'

"""
named created folders to process "down"

"""

shift_down = 'data/shift_down/'
crop_mirror_down = 'data/crop_mirror_down/'
paste_down = 'data/paste_down/'




dirs = os.listdir( path )

def shift_images(y): #this function is shifting images in all directions and saving them in different folders

   
    for item in tqdm(dirs):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            file, ext = os.path.splitext(shift_up+item)
            a = 1
            c = 0
            b = 0
            d = 0
            e = 1
            f = y-1 #10 pixels up (image moved 10px up so bottom of the image is blank black rectangular (up/down)
            translate = im.transform(im.size, Image.AFFINE, (a,b,c,d,e,f))
            translate.save(file + '.png', quality=100)
            file1, ext = os.path.splitext(crop_mirror_up+item)
            w, h = im.size
            cropped_im = im.crop((0, w-h+y , w, h))  #(left,up,right,bottom)
            cropped_im.save(file1 + '.png', quality=100)
            rotated_im = cropped_im.transpose(Image.FLIP_TOP_BOTTOM)
            image_copy = rotated_im.copy()
            position = ((0,h-y))
            im = Image.open(shift_up+item)
            im.paste(image_copy, position)
            file3, ext = os.path.splitext(paste_up+item)
            im.save(file3 + '.png', quality=100)        
    shutil.rmtree('data/shift_up')
    shutil.rmtree('data/crop_mirror_up/')               
    print("'Up' folder has been created successfully") 
    
    for item in tqdm(dirs):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            file, ext = os.path.splitext(shift_right+item)
            c = -y # 10 pixels right (image moved 20px right so on the left side there is a blank black rectangular)
            a = 1
            b = 0
            d = 0
            e = 1 
            f = 0
            translate = im.transform(im.size, Image.AFFINE, (a,b,c,d,e,f))
            translate.save(file + '.png', quality=100)
            file, ext = os.path.splitext(crop_mirror_right+item)
            w, h = im.size
            cropped_im = im.crop((0, 0, y, h))  #(left,up,right,bottom)
            rotated_im = cropped_im.transpose(Image.FLIP_LEFT_RIGHT)
            image_copy = rotated_im.copy()
            position = ((0,0))
            im = Image.open(shift_right+item)
            im.paste(image_copy, position)
            file3, ext = os.path.splitext(paste_right+item)
            im.save(file3 + '.png', quality=100)
            #rotated_im.save(file + '.png', quality=100)
            #cropped_img.save(file + '.png', quality=100
    shutil.rmtree('data/shift_right')
    shutil.rmtree('data/crop_mirror_right/') 
    print("'Right' folder has been created successfully") 
    
    for item in tqdm(dirs):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            file, ext = os.path.splitext(shift_left+item)
            c = y # 10 pixels left (imge moved 10 px left so left side is balnk black rectangular)
            a = 1
            b = 0
            d = 0
            e = 1
            f = 0
            translate = im.transform(im.size, Image.AFFINE, (a,b,c,d,e,f))
            translate.save(file + '.png', quality=100)
            file, ext = os.path.splitext(crop_mirror_left+item)
            w, h = im.size
            cropped_im = im.crop((w-y, 0, w, h))      
            rotated_im = cropped_im.transpose(Image.FLIP_LEFT_RIGHT)
            #rotated_im2 = rotated_im.transpose(Image.FLIP_LEFT_RIGHT)
            image_copy = rotated_im.copy()
            position = ((w-y,0))
            im = Image.open(shift_left+item)
            im.paste(image_copy, position)
            file3, ext = os.path.splitext(paste_left+item)
            im.save(file3 + '.png', quality=100)
    shutil.rmtree('data/shift_left')
    shutil.rmtree('data/crop_mirror_left/') 
    print("'Left' folder has been created successfully") 
        
    for item in tqdm(dirs):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            file, ext = os.path.splitext(shift_down+item)
            a = 1
            c = 0
            b = 0
            d = 0
            e = 1
            f = -y #10 pixels down (image moved 10px down so top of the image is blank black rectangular (up/down)
            translate = im.transform(im.size, Image.AFFINE, (a,b,c,d,e,f))
            translate.save(file + '.png', quality=100)
            file, ext = os.path.splitext(crop_mirror_down+item)
            w, h = im.size
            cropped_im = im.crop((0, 0, w, y))  #(left,up,right,bottom)
            rotated_im = cropped_im.transpose(Image.FLIP_TOP_BOTTOM)
            image_copy = rotated_im.copy()
            position = ((0,0))
            im = Image.open(shift_down+item)
            im.paste(image_copy, position)
            file3, ext = os.path.splitext(paste_down+item)
            im.save(file3 + '.png', quality=100)
            #rotated_im.save(file + '.png', quality=100)
    shutil.rmtree('data/shift_down')
    shutil.rmtree('data/crop_mirror_down/')
    print("'Down' folder has been created successfully") 
    
    


shift_images(10) 





