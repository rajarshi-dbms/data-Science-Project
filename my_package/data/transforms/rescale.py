#Imports
import PIL
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if not isinstance(image,PIL.Image.Image):
            image = Image.fromarray(image)
            
        r = image
        if isinstance(self.size,tuple):
          r = image.resize(self.size)
        if isinstance(self.size,int) :
          h, w = image.size
          r = image.resize(((self.size * h) , self.size * w))

        if isinstance(self.size,float) :
          h, w = image.size
          r = image.resize((int(self.size * h) , int(self.size * w)))
        
        return r
