from PIL import Image
from numpy import asarray
import numpy as np
import random
import glob
import time
import os.path
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# load the image
def image_load(images):
    image_python_object = {
    }
    i=0
    for image in images:
        image_array = Image.open(image)
        data = asarray(image_array)

        image_number = "image"+str(i)
        image_python_object[image_number] = data
        i=i+1
    return image_python_object

def run_checks(ratio,image_python_object):
    if len(ratio) != len(image_python_object):
        print("ratio must be same have as many items as images" )
        quit()
    if sum(ratio) != 1000:
        print("ratio must equal 1000 but ratio is " + str(ratio))
        quit()

def create_lines_image(image_python_object,ratio,thickness):
    run_checks(ratio,image_python_object)
    width= len(image_python_object ['image0'][0])
    height = len(image_python_object ['image0'])
    image_type = len(image_python_object ['image0'][0][0])
    new_img = np.zeros(shape=(height,width,image_type),dtype='int8')

    i=1
    rand_number = random.randint(0, 100)
    while i != height:
        if i % thickness == 0:
            rand_number=random.randint(0, 100)
        total_ratio = 0
        y = 0
        for image in image_python_object:
            if rand_number in range(total_ratio,total_ratio+ratio[y]):
                line = image_python_object[image][i]
            total_ratio = total_ratio+ratio[y]
            y=y+1
        new_img[i] = line
        i=i+1
    print(new_img)
    create_new_img = Image.fromarray(new_img, 'RGB')
    create_new_img.show()

def randomizer_images(image_python_object,ratio,rand_number):
    total_ratio = 0
    y = 0
    for image in image_python_object:
        if rand_number in range(total_ratio, total_ratio + ratio[y]):
            return image
        total_ratio=total_ratio+ratio[y]
        y = y + 1

def create_rand_image(image_python_object, ratio, thickness,save_location,image_data):
    run_checks(ratio, image_python_object)
    width = len(image_python_object['image0'][0])
    height = len(image_python_object['image0'])
    image_type = len(image_python_object['image0'][0][0])
    new_img = np.zeros(shape=(height, width, image_type), dtype=image_python_object['image0'].dtype)

    row = 0
    line = []
    pixel_number = 0
    rand_number = random.randint(0, 100)
    while row != height:
        col=0
        while col != width:
            pixel_number = pixel_number+1
            if pixel_number % thickness == 0:
                rand_number = random.randint(0, 999)
            random_image = randomizer_images(image_python_object,ratio,rand_number)
            pixel = image_python_object[random_image][row][col]
            line.append(pixel)
            col = col+1
        new_img[row] = line
        line = []
        row = row+1
        clear()
        if image_data != None:
            for data in image_data:
                print(str(data))
        print(str(row)+"/"+str(height))

    create_new_img = Image.fromarray(new_img, 'RGB')
    #create_new_img.show()
    create_new_img.save(save_location)


def chaos(folder_location,width,limit):
    images_array = []

    i = len(glob.glob('D:\\python projects\\imag_man\\chaos' + '/*'))
    for image_file_loc in glob.glob(folder_location + '/*'):
        images_array.append(image_file_loc)
    print(len(images_array))
    while i<limit:
        rand_selected_images = []
        random.shuffle(rand_selected_images)
        for x in range(random.randint(2, len(images_array))):
            rand_selected_images.append(images_array[random.randint(1, len(images_array)-1)])

        total_ratio=1000
        ratio = []
        for x in range(len(rand_selected_images)):
            if x+1!=len(rand_selected_images):
                rand_ratio=random.randint(0, round(total_ratio*0.8,0))
                ratio.append(rand_ratio)
                total_ratio=total_ratio-rand_ratio
                print(x)
            else:
                ratio.append(total_ratio)

        loaded_images = image_load(rand_selected_images)
        pixel_width = random.randint(1, width)
        create_rand_image(loaded_images,ratio,pixel_width,'chaos/image_'+str(i)+'.jpg',["image number "+str(i),"amount of merged Images "+str(len(rand_selected_images)),"ratio of "+str(ratio),"random Pixel width "+ str(pixel_width)])
        i=i+1

if __name__ == "__main__":
    #testing = image_load(['images/image_1.jpg','images/image_2.jpg'])
    #create_lines_image(testing,[30,70],5)
    #create_rand_image(testing,[50,50],100,'images/test.jpg')
    #video_mix('farm1','farm2')
    chaos('image_resize\size2048_1536',50,200)