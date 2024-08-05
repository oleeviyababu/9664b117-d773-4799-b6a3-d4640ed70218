#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
filenames = listdir("pet_images/")
for i in range(0, len(filenames)):
  filenames[i] = filenames[i].lower()
  filenames[i] = filenames[i].split("_")
  pet_label = ""
  for word in filenames[i]:
    if word.isalpha():
      pet_label+=word+" "
  pet_label = pet_label.strip() 
  print("\nFilename=", filenames[i], "   Label=", pet_label)

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    filenames = listdir(image_dir)
    
    results_dic = {}
    
    # Process each file in the directory
    for filename in filenames:
        if filename.startswith('.'):
            continue
        
        pet_label = ''
        words = filename.lower().split('_')
        
        for word in words:
            if word.isalpha():
                pet_label += word + ' '
        
        pet_label = pet_label.strip()
        
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Key=", filename, "already exists in results_dic with value =", results_dic[filename])
    
    return results_dic

 
  