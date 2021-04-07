from main import *
def image_resize_folder(folder_location,resize_size):
    i=0
    amount_of_images=str(len(glob.glob(folder_location + '/*')))
    for image_file_loc in glob.glob(folder_location + '/*'):
        try:
            image = Image.open(image_file_loc)
            width, height = image.size
            extension = os.path.splitext(image_file_loc)[1]
            traget_folder_name = "image_resize/size" + str(width) + '_' + str(height)
        except:
            pass
        try:
            os.makedirs(traget_folder_name)
            image.save(traget_folder_name+'/image_' + str(i) + extension)
        except FileExistsError:
            image.save(traget_folder_name+'/image_' + str(i) + extension)
        print(str(i) + '/' + amount_of_images)
        i=i+1