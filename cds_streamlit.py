import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px
import geopandas as gpd
from matplotlib import font_manager, rc

#pip install mpld3 html 저장 위해

import mpld3

import streamlit as st
import pandas as pd

# Z 드라이브의 데이터 파일 경로
file_path = 'Z:/private/dsi/streamlit/data.csv'

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    return data

data = load_data(file_path)

# Streamlit 대시보드 구성
st.title('NAS 데이터를 이용한 Streamlit 대시보드')
st.write('데이터 미리보기:')
st.write(data.head())

# 그래프 예시
#st.line_chart(data)