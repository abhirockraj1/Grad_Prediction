import streamlit as st
import numpy as np


st.title('Predict the chance of getting Graduated from top University :question:')

greS = st.number_input('Enter GRE SCORE ',min_value=290.00,max_value=340.00)
tofelS = st.number_input('Enter TOEFL SCORE ',min_value=92.00,max_value=120.00)
urS = st.number_input('Enter University Rating', min_value=1.00,max_value=5.00)
sopS = st.number_input('Enter SOP ', min_value=1.00,max_value=5.00)
lorS = st.number_input('Enter LOR ', min_value=1.00,max_value=5.00)
gpaS = st.number_input('Enter GPA SCORE ', min_value=6.8,max_value=9.20)
reS = st.number_input('Enter Research SCORE ', min_value=0.00,max_value=1.00)



x = np.array([1.0,(greS-316.47)/(11.29**2),(tofelS-107.19)/(6.08**2),(urS-3.11)/(1.14**2),(sopS-3.37)/(0.99**2),(lorS-3.48)/(0.92**2),(gpaS-8.57)/(0.60**2),(reS-0.56)/(0.49**2)])
x= np.reshape(x,(x.shape[0],1))

th_data = np.loadtxt("weight.txt", delimiter=",",dtype=float)
th_data = np.reshape(th_data,(1,th_data.shape[0]))
# print(th_data)

extra = np.exp(-np.dot(th_data,x))
yhat = 1/(1+extra)
# print( yhat[0][0])
yhat = round(yhat[0][0]*100.0, 2)

if st.button('Calculate'):
    if(yhat>=60.0):
        st.write(yhat,' % Chance to get into an University good job :sunglasses:')
    elif(yhat>=50.0 and yhat<=60.0):
        st.write(yhat,' % Chance to get into an University be optimistic :cold_sweat:')
    else:
        st.write(yhat,' % Chance to get into an University, work hard for next year :worried:')
else:
    st.write('Check your Entry percentage into university')