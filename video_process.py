import cv2
import glob
import os
from main import *
def getFrame(sec,vidcap,count,folder_name):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("video_images/"+folder_name+"/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
def video_to_image(video,frame_rate,folder_name):
    #try:
     #   os.makedirs("video_images/"+folder_name)
    #except FileExistsError:
     #   print('folder already exists')
      #  quit()
    vidcap = cv2.VideoCapture(video)
    sec = 0
    frameRate = 1/frame_rate
    count=1
    success = getFrame(sec,vidcap,count,folder_name)
    while success:
        print(count)
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,vidcap,count,folder_name)
def image_to_videos(image_path,frame_rate):
    img_array = []
    # glob.glob() fetches the filename of all the jpg files present in that path
    number_of_images=len(glob.glob(image_path + '/*.jpg'))
    i=1
    while i != number_of_images:
        print('loading'+'image'+str(i))
        img = cv2.imread(image_path + '/image'+str(i)+'.jpg')
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
        i= i+1


    out = cv2.VideoWriter('project.avi', 0, frame_rate, size)

    for i in range(len(img_array)):
        print('writing' + str(i))
        out.write(img_array[i])
    out.release()

def video_mix(folder_name1,folder_name2):
    imagenumber=0
    i=0
    while i != imagenumber:
        testing = image_load(['video_images/'+folder_name1+'/image'+str(i)+'.jpg','video_images/'+folder_name2+'/image'+str(i)+'.jpg'])
        create_rand_image(testing,[50,50],100,'video_images/temp/image'+str(i)+'.jpg')
        i=i+1
        print(i)
    image_to_videos('video_images/temp',30)

if __name__ == "__main__":
    #video_to_image('video1.mp4',30,'farm1')
    video_to_image('slowthai .mp4',30,'slowthai')
    #image_to_videos('video_images/temp',30)
