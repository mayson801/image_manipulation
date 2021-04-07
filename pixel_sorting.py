from main import *
from tabulate import tabulate
import sys


def pixel_sort(image,save_location,sort_frequency_range,randomness):
    i=0
    height = np.size(image, 0)
    width = np.size(image, 1)
    new_image = np.empty(shape=(height,width,3), dtype='int8')
    new_line_section=[]


    for line in image:
        new_line_section = []
        converted_line=[]
        if randomness==True:
            sort_frequency = random.randint(1, sort_frequency_range)
        else:
            sort_frequency=sort_frequency_range
        for count, pixel in enumerate(line.tolist()):
            new_line_section.append(pixel)
            if count % sort_frequency == 0:
                if 10<random.randint(1, 100):
                    new_line_section.sort()
                for pixel in new_line_section:
                    converted_line.append(pixel)
                    new_line_section = []
            elif count==width-1:
                if 10<random.randint(1, 100):
                    new_line_section.sort()
                for pixel in new_line_section:
                    converted_line.append(pixel)
                    new_line_section = []
        converted_line = np.asarray(converted_line)
        converted_line = converted_line.reshape(1,width,3)

        new_image[i, :] = converted_line[0, :]

        i=i+1
        #print('image number ' + str(save_location))
        #print('image_progress' + str(i)+'/'+str(height))

    create_new_img = Image.fromarray(new_image, 'RGB')
    create_new_img.save(save_location)

def print_as_table(data,rows):
    headers = []
    for x in range(rows):
        headers.append("col_"+str(x))
        print(x)

    # tabulate data
    table = tabulate(data[0], headers, tablefmt="fancy_grid")

    # output
    print(table)
if __name__ == "__main__":
    i=365
    limit=6635
    while i!=limit:
        testing = image_load(['video_images/slowthai/image'+str(i)+'.jpg'])
        pixel_sort(testing['image0'],'video_images/slowthai_adapt/image'+str(i)+'.jpg',60,True)
        clear()
        print(str(i)+'/'+str(limit))
        i=i+1
