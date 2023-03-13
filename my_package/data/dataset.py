#Imports
import json
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
     
        self.transforms = transforms
        with open(annotation_file, 'r+') as f:
            jsonlist = list(f)
        self.lt = []
        for string in jsonlist:
            self.lt.append(json.loads(string))
    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.lt)

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        index = self.lt [idx]
        jpg = "data/imgs/"+index["file_name"]
        url = index["url"]
        return (jpg,url)
        

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        im = []
        img = Image.open(path)
        if self.transforms != None:
            for instanceTransform in self.transforms:
                imon = instanceTransform (img)
                im.append(imon)
        return im