import tensorflow as tf 
import keras as K
import numpy as np
from flask import Flask, request, jsonify
import streamlit as st

# app = Flask(__name__)

# @app.route('/predict',methods=['POST'])
# def predict():

#     Brand = float(request.form.get('brand'))
#     Processor_Speed	= float(request.form.get('processor'))
#     RAM_Size = float(request.form.get('ram'))
#     Storage_Capacity = float(request.form.get('storage'))
#     Screen_Size	= float(request.form.get('screen'))
#     Weight = float(request.form.get('weight'))

#     print(Brand,type(Weight))

#     model = K.models.load_model('demo_app.h5')
#     inp = tf.constant([[Brand,Processor_Speed,RAM_Size,Storage_Capacity,Screen_Size,Weight]])
#     pred = model.predict(x=inp)

#     result = {'pred' : str(pred)}

#     return jsonify(str(pred))






if __name__ == '__main__':
    #app.run(debug=True)

    def stmapp():

        st.title('Predict laptop Price')
        st.write('### Please input the following values')

        Brand = st.text_input(label='Brand',value='',key='brand')
        Processor_Speed	= st.text_input(label='Processor_speed',value='',key='processor_speed')
        RAM_Size = st.text_input(label='Ram_Size',value='',key='ram')
        Storage_Capacity = st.text_input(label='Storage_capacity',value='',key='Storage')
        Screen_Size	= st.text_input(label='Screen_Size',value='',key='screen_size')
        Weight = st.text_input(label='Weight',value='',key='Weight')

        if st.button('Predict'):
            try:
                Brand = float(Brand)
                Processor_Speed = float(Processor_Speed)
                RAM_Size = float(RAM_Size)
                Storage_Capacity = float(Storage_Capacity)
                Screen_Size = float(Screen_Size)
                Weight = float(Weight)
                model = K.models.load_model('demo_app.h5')
                inp = tf.constant([[Brand,Processor_Speed,RAM_Size,Storage_Capacity,Screen_Size,Weight]])
                pred = model.predict(x=inp)
                output = pred[0][0]
            except Exception as e:
                print('Enter values :',e)
        
            st.write(f'The estimated price is $ {output:.2f}')
            print(Brand)



    stmapp()

