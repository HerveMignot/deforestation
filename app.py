import random

import streamlit as st

from PIL import Image

def classify_image(image) -> bool:
    """Classify if an image has palm trees or not
    
    Params:
    - image (bytes): image to be classify
    
    Returns:
    - bool: True if image contains palm trees
    """
    return random.choice([True, False])
    

def analyze_image(image):
    """Analyze parts of image that most contributed to classification
    
    Params:
    - image (bytes): image to analyze
    
    Returns:
    - bytes: image showing most contributive part of the image
    """
    return Image.open(image).convert("L")
    

st.write("## Palm Tree Dectector")

with st.sidebar:
    image_file = st.file_uploader('Choose an image',
                                  type=['png', 'jpg'],
                                  help='Select image to be classified',
                                 )

if image_file is not None:
    bytes_image = image_file.getvalue()
    st.image(bytes_image, width=256)

if st.button('Detect palm trees', disabled=(image_file is None)):
    result = classify_image(bytes_image)
    if result:
        st.write('Palm trees detected')
    else:
        st.write('Palm trees not detected')

    with st.expander('Sensitivity Analysis', expanded=False):
        analysis_image = analyze_image(image_file)
        st.image(analysis_image, width=256)
