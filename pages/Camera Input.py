import streamlit as st
from PIL import Image
import numpy as np

enable = st.checkbox('Enable Camera')
if enable:
    picture = st.camera_input('Picture')
