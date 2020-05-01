'''
Created on 07-Dec-2019

@author: DELL
'''

class Node:
    def __init__(self, data):
        self.__data=data
        self.__next=None
      
    def get_data(self):
        return self.__data
  
    def set_data(self, data):
        self.__data = data
    
    def get_next(self):
        return self.__next
  
    def set_next(self, next_node):
        self.__next = next_node
