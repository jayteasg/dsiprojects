import streamlit as st

import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

size = (100,100)

def select_veg(pred, df):
    veg_list = {}
    for idx in range(2):
        #veg_list.append(pred.index[idx])
        veg_list[pred.index[idx]] = 1

        # Are there any similar vegetable
        if df.loc[pred.index[idx],'similar']!="none":
            #veg_list.append(df.loc[pred.index[idx],'similar'])
            veg_list[df.loc[pred.index[idx],'similar']] = 1

    option = st.radio('Choose one:', (list(veg_list.keys())))
    return option

file = st.file_uploader("Upload an image",type=["jpg","png","jpeg"])
if file is not None:
    st.image(file, width=400)
    pic = Image.open(file)

    # load production model
    model_prod = load_model('./models/prod_model.hdf5')

    # Load imagenet weights
    conv_base = VGG16(weights='imagenet',
                      include_top=False,
                      input_shape=(100, 100, 3))  # 3 = number of channels in RGB pictures

    # Load the classes
    infile = open('./models/veg_class.pkl','rb')
    veg_df = pickle.load(infile)
    infile.close()

    # Load the vegetable prices
    price_df = pd.read_csv('./datasets/price_per_kg.csv', index_col=0)

    # Load the similar vegetables file
    similar_df = pd.read_csv('./datasets/similar_vegetables.csv', index_col=0)

    # Resize image to 100x100
    if pic.size[0] == pic.size[1]: #square
        pic = ImageOps.fit(pic, size, Image.ANTIALIAS)
    else:
        (w,h) = pic.size
        if w>h:
            pic = ImageOps.fit(pic, size, centering=(0.5,0))
        else:
            pic = ImageOps.fit(pic, size, centering=(0,0.5))

    # Standardize to 0 to 1 and reshape for model
    pic = np.array(pic)/255
    pic = pic.reshape(1,100,100,3)

    # Feature extraction
    features = conv_base.predict(pic)

    # Prediction
    pred = pd.Series(model_prod.predict(features)[0], index=veg_df.index).sort_values(ascending=False)[:2]

    option = select_veg(pred, similar_df)

    #checking prediction result
    if st.button("Print Label"):
        price_per_kg = price_df.loc[option,'price_per_kg']
        weight = np.random.randint(1,100)/100
        total_price = price_per_kg * weight

        st.write(option + '\n' + '-' * 30)
        st.write(f'PRICE/KG: ${price_per_kg}')
        st.write(f'WEIGHT: {np.round(weight,3)} kg')
        st.write(f'TOTAL PRICE: ${np.round(total_price,2)}')
