#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.flip == "vertical" : 
            return image.transpose(method = Image.FLIP_LEFT_RIGHT)
        else :
            return image.transpose(method = Image.FLIP_TOP_BOTTOM)
        
# Testing

if __name__ == "__main__" :
    img  = Image.open("a.jpeg")
    flip = FlipImage("vertical")
    img = flip(img)
    # img2 = asarray(img.convert("RGB"))
    # print(img2.shape)
    img.show()