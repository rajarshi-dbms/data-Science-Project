#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from my_package.data import Dataset , Download
import numpy as np
from PIL import Image
import os


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    data = Dataset(annotation_file=annotation_file, transforms= transforms )
    load = Download()

    #Print image names and their captions from annotation file using dataset object
    for idx in data.lt :
        print ("file :"+idx["file_name"]+"\n")
        print (idx["captions"])
    i=0
    #Download images to ./data/imgs/ folder using download object

    while i < 10 :
        x =data.__getann__(i)
        load(x[0] ,x[1] )
        i+=1

    #Transform the required image (roll number mod 10) and save it seperately
    item =data.__transformitem__("data/imgs/0.jpg")
    i = 0
    for im in item:
        s = "% s" % i
        x = im.save(outputs+"0"+s+".jpg")
        i+=1

    #Get the predictions from the captioner for the above saved transformed image  
    caption = captioner("data/imgs/0.jpg",3)
    print ("Original:")
    print (caption)
    im = Image.open(("data/imgs/0.jpg"))
    x = [FlipImage('horizontal'),BlurImage(3), RescaleImage(2), RescaleImage(0.5), RotateImage(-90), RotateImage (45)]
    data.transforms = x
    im =data.__transformitem__("data/imgs/0.jpg")
    n = i
    for y in x:
        s = "% s" % i
        print (s+")")
        im[i - n].save(outputs+"/0"+s+".jpg")
        i+=1
        caption = captioner(outputs+"/0"+s+".jpg", 3)
        print (caption)

def main():
    captioner = ImageCaptioningModel()
    outputs = os.path.dirname(os.path.realpath(__file__)) + "/output"
    if not os.path.exists(outputs):
        os.makedirs(outputs)
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], outputs) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()