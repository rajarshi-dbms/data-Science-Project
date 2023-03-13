from PIL import Image
import requests
from io import BytesIO
import shutil

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
        if isinstance(url ,str):
            req = requests.get(url, stream = True)
            
            if req.status_code == 200:
                req.raw.decode_content = True
                with open( path, 'wb') as f:
                    req.raw.decode_content = True
                    shutil.copyfileobj( req.raw, f)
