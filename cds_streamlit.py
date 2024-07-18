import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px
import geopandas as gpd
from matplotlib import font_manager, rc

# GitHub raw content URL의 data.csv 파일 경로
file_path = 'https://raw.githubusercontent.com/cdshadow/public1/main/data.csv'

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

# 연도와 월을 합쳐서 'Date' 열을 생성 (day를 1로 설정)
data['Date'] = pd.to_datetime(data[['년도', '월']].assign(day=1))

# 소계 열을 'Sum'으로 변경
data.rename(columns={'소계': 'Sum'}, inplace=True)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['Date'], data['Sum'])
ax.set_xlabel('Date')
ax.set_ylabel('Sum')
ax.set_title('Monthly Sum')

st.pyplot(fig)
