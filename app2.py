import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# # Image
st.title("Image")
# img = Image.open('panda.png')
# st.image(img, width=500)

# # video
# st.title("video")
# video_file = open('1.mp4', 'rb')
# st.video(video_file, start_time=20)

# # audio
# # st.title("audio")
# # audio_file = open('https://wynk.in/music/song/sweet-nothing/um_00602448638793-USUG12205718', 'rb')
# # st.audio(audio_file, start_time=20)

# # CSV Files
# df = pd.read_csv('random data_set.csv')

# st.title('displaying the head of data_frame')
# st.dataframe(df.head())

# st.title('displaying the data_frame in table format')
# st.table(df.head(10))

# st.title("displaying JSON File")
# js = [{'pid': 1, 'name': '5 star'},
#       {'pid': 2, 'name': '4 star'},
#       {'pid': 3, 'name': '3 star'},
#       {'pid': 4, 'name': '2 star'}]

# st.json(js)


# # uploading files
st.title('uploading image')
img_file = st.file_uploader('upload any image', type=['jpeg', 'png','jpg'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type': img_file.type, 
                    'file_size': img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))


# # st.title('uploading audio')
# # audio_file = st.file_uploader('upload any audio', type=['wav', 'mp3'])
# # if audio_file is not None:
# #     file_details = {'file_name' : img_file.name, 'file_type': img_file.type, 
# #                     'file_size': img_file.size}
# #     st.write(file_details)
# #     st.image(Image.open(img_file))


st.title('uploading video')
video_file = st.file_uploader('upload video', type=['mov', 'mp4'])
if video_file is not None:
    file_details = {'file_name': video_file.name, 'file_type': video_file.type, 
                    'file_size': video_file.size}
    st.write(file_details)
    st.video(video_file)



# # Image Converter (eg: from jpg -> png , etc)
# # st.title('image converter')
# # image_file = st.file_uploader('upload ur image that u want to convert', type=['png', 'jpeg', 'jpg'])

# # new_format = st.selectbox('select the output format', ['png', 'jpeg', 'jpg'])


# # def convert_image(image_path, new_format):
# #     with Image.open(image_path) as img:
# #         img.save(img.name)

        
# # if st.button('convert'):
# #     if image_file is not None:
# #         convert_image(image_file, new_format)
# #     else:
# #         st.error('please upload an image file of the following type')



# # Image Rotation
# import cv2 as cv

# def rotate_image(image, angle):
#     img = np.array(image)
#     height, width = img.shape[:2]
#     M = cv.getRotationMatrix2D((width/2, height/2), angle,10)
#     rotate_img = cv.warpAffine(img, M, (width, height))
#     return rotate_img

# st.title("Image rotation")
# st.subheader("upload an img")

# img_file = st.file_uploader('upload ur img', type=['.jpeg', '.jpg', 'png'])

# st.subheader('rotate the img')
# angle = st.slider('choose the angle:', -180, 180, 0, 1)

# if img_file is not None:
#     image = Image.open(img_file)
#     rotated_img = rotate_image(image, angle)
#     st.image(rotated_img)
# else:
#     st.subheader("Plz upload the img")
