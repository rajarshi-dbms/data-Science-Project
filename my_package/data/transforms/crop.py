#Imports
import cv2
import random
import numpy as np
import PIL
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.crop = crop_type
        self.array = shape

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if isinstance(image,PIL.Image.Image):
            im = np.asarray(image)
        else :
            if isinstance(image,np.ndarray):
                im = image
            else : return
        w = self.array[0]
        h = self.array[1]
        x = random.random()*h/2
        y = random.random()* w/2
        if self.crop == 'center' :
            er = im [int (w*0.25):int (w*0.75), int (h*0.25):int (h*0.75)]
        else :
            n = int (w*(0.25)  + y) % w if int (w*(0.25)  + y) % w < (int (w*(0.75 ) + y )) % w else (int (w*(0.75 ) + y )) % w
            m = int (w*(0.25)  + y) % w if int (w*(0.25)  + y) % w > (int (w*(0.75 ) + y )) % w else (int (w*(0.75 ) + y )) % w
            o = (int (h*(0.25) + x)) % h if (int (h*(0.25) + x)) % h < (int (h*(0.75) + x) % h) else (int (h*(0.75) + x) % h)
            p = (int (h*(0.25) + x)) % h if (int (h*(0.25) + x)) % h > (int (h*(0.75) + x) % h) else (int (h*(0.75) + x) % h)
            er = im [n : m , o : p ]
        return PIL.Image.fromarray(np.uint8(er))

# Testing

'''if __name__ == "__main__" :
    img  = Image.open("a.jpeg")
    crop = CropImage((350,300),"center")
    img = crop(img)
    # img2 = asarray(img.convert("RGB"))
    # print(img2.shape)
    img.show()'''
 
