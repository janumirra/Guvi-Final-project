# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 08:48:14 2022

@author: Sundaram
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image
#import json
#import requests
#from streamlit_lottie import st_lottie


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Sundaram/Jupyter notebook folder/GUVI final project/breast_cancer_trained_model.sav', 'rb'))


# creating a function for Prediction

def cancer_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    #if data need to be scaled do it here
    #input_data_reshaped = std.transform(input_data_reshaped)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is cancer-free'
    else:
      return 'The person has cancer'
  
    
  
def main():
    
    #image
    image=Image.open('C:/Users/Sundaram/Jupyter notebook folder/GUVI final project/Breast cancer prediction.jpg')
    st.image(image,
             use_column_width=True)
    
    
  
    
    
    # giving a title
    st.title('Breast cancer Prediction Web App')
    
 
    
    
    # getting the input data from the user
    radius_mean =st.text_input('radius')
    texture_mean =st.text_input('texture')
    perimeter_mean=st.text_input('perimeter')
    area_mean=st.text_input('area')
    smoothness_mean=st.text_input('smoothness')
    compactness_mean=st.text_input('compactness')
    concavity_mean=st.text_input('concavity')
    concave_points_mean=st.text_input('concave points')
    symmetry_mean=st.text_input('Symmetry')
    fractal_dimension_mean=st.text_input('fractal dimension')
    
    
  
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cancer Test Result'):
        diagnosis = cancer_prediction([radius_mean, texture_mean, perimeter_mean,area_mean, smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    