import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px
import geopandas as gpd
from matplotlib import font_manager, rc

# GitHub raw content URL의 data.csv 파일 경로
file_path = 'https://raw.githubusercontent.com/cdshadow/import_streamlit/main/data.csv'

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    return data

data = load_data(file_path)

# 데이터 확인
st.write("2001년~2023년 대전시 순이동")
st.table(data[['시점', '데이터']].reset_index(drop=True))

#st.dataframe(data[['시점', '데이터']].reset_index(drop=True))

# 데이터를 리스트로 변환하여 출력
# st.write(data[['시점', '데이터']].values.tolist())

#st.write(data.head())
