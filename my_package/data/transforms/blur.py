#Imports
import PIL
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius
  

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        
        if not isinstance(image,PIL.Image.Image):
            im = Image.fromarray(image)

        return image.filter(ImageFilter.GaussianBlur(self.radius))

# Testing

if __name__ == "__main__" :
    im  = Image.open("a.jpeg")
    blur = BlurImage(1)
    im = blur(im)
    # img2 = asarray(img.convert("RGB"))
    # print(img2.shape)
    im.show()
