#!/usr/bin/env python
#*-* coding: utf-8 *-*
from __builtin__ import file
import os.path
import sys
import pandas as pd
import numpy as np
import scipy as sp
import constants as cs
import matplotlib.pyplot as plt


class DCB_generation:
        def __init__(self, selected_dcb):   
            with open(selected_dcb, 'r+') as DCB_file:
                contents = DCB_file.readlines()
                
            self.dcb_dictionary = self.read_dcb_file(contents)
                
        def read_dcb_file(self, contents):
            column_name_list = []
            
            for lineNumber, line in enumerate(contents):
                label = line[0:3]
                if label == 'PRN':
                    modifiedDCB_file = contents[lineNumber +2:]    
                    break  

            dcb_dictionary = self.read_dcb_values(modifiedDCB_file, column_name_list)
            
            return dcb_dictionary

            
        def read_dcb_values(self, modifiedDCB_file, column_name_list):
            prn_list = []
            dcb_values_list = []
    
            for i in modifiedDCB_file:
                line_components = i.split()            
                if len(line_components) == 0:
                    break
                first_column = line_components[0]
                if len(first_column) == 1:
                    break
                prn_list.append(first_column)
                dcb_values_list.append(float(line_components[1]))
                
            dcb_in_metres = self.nanosecond_to_metres(dcb_values_list)
            dcb_dictionary = dict(zip(prn_list, dcb_in_metres))

            return dcb_dictionary
            
            
        def nanosecond_to_metres(self, dcb_values_list):
            dcb_in_metres = []
            
            for i in dcb_values_list:
                dcb_metres = i * cs.LIGHT_V * 10**-9
                dcb_in_metres.append(dcb_metres)
                
            return dcb_in_metres

if __name__ == '__main__':

    path = "/home/holdder/Timestamps/"

    


    
        
   