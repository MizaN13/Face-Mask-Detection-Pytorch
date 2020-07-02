# -*- coding: utf-8 -*-
"""DataPreprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iZLQ3IqfMJ-DBVLYl4J9KPZInf_xoGxW

#Data Preprocessing
"""

#Importing required libraries

from torchvision.datasets import ImageFolder
from torchvision import transforms
import numpy as np
import torch

class Preprocessing():
    # This class will transforms every images into the applied transforms.
    # And it returns the dataset as tensor dataset and the categories

    def __init__(self, path=None, img=None):
        '''
        params: path: (str) directory to the image folder
        params: array: (array) image array
        '''
        self.directory = path
        self.img = img
    
    def __image_transformation(self):
        '''
        params: None
        return: transformations
        '''
        transform = transforms.Compose([
                transforms.Resize((130,130)),
                transforms.CenterCrop(128),
                transforms.Grayscale(1),
                transforms.ToTensor(),
                transforms.Normalize(0.5,0.5)
        ])
        return transform
    
    
    def preprocessed_arrays(self):
        #For predicting
        '''
        params: None
        return: (array) single Tensor data
        '''
        img = self.img
        transforms =  self.__image_transformation()
        return torch.tensor(np.expand_dims(transforms(img),0))

    def preprocessed_dataset(self):
        '''
        params: None
        return: Tensor dataset
        '''
        #Using torch's ImageFolder to get data from directory and applying
                                                                #transforms
        transformations =  transforms.Compose([
                transforms.RandomHorizontalFlip(),
                transforms.RandomPerspective(0.2,p=0.5),
                self.__image_transformation()])
        
        dataset_train = ImageFolder(self.directory['train'], 
                                transform= transformations)
        dataset_test = ImageFolder(self.directory['test'], 
                                transform=  self.__image_transformation())
        
    
        return dataset_train, dataset_test

