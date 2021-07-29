import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime

# Configuration
st.set_page_config(layout="wide")
st.set_option('deprecation.showfileUploaderEncoding', False)
# Title
st.title("Dashboard")

# Sidebar
st.sidebar.subheader("Control Panel")

# File upload
uploaded_file = st.sidebar.file_uploader(label="Upload a CSV or Excel file", type=['csv', 'xlsx'])

global df
global numeric_columns

if uploaded_file is not None:
    print(f"{datetime.now()} - File Uploaded")
    try:
        df = pd.read_csv(uploaded_file)
        df = df.dropna()
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
        df = pd.read_excel(uploaded_file)
        df = df.dropna()

try:
    st.info(f"File: {uploaded_file.name}")
    with st.beta_expander("Expand Data"):
        st.table(df)
    numeric_columns = list(df.select_dtypes(['float', 'int', 'object']).columns)
except Exception as e:
    print(f"{datetime.now()} - ERROR: {e}")
    st.warning("No file uploaded")

# Chart type selectbox
chart_select = st.sidebar.selectbox(label="Chart Type",
                                    options=['Scatter Plot', 'Line Plot', 'Area Plot', 'Bar Chart',
                                             'Histogram', 'Mapbox', 'Geo Scatter Plot', 'Pie Chart'])
# Scatter Plot
if chart_select == 'Scatter Plot':
    st.sidebar.subheader("Scatter Plot Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("X-axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, title=chart_title, width=width, height=height, template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Line Plot
if chart_select == 'Line Plot':
    st.sidebar.subheader("Line Plot Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("X-axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.line(data_frame=df, x=x_values, y=y_values, title=chart_title, width=width, height=height, template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Area Plot
if chart_select == 'Area Plot':
    st.sidebar.subheader("Area Plot Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("X-axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.area(data_frame=df, x=x_values, y=y_values, title=chart_title, width=width, height=height, template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Bar Chart
if chart_select == 'Bar Chart':
    st.sidebar.subheader("Bar Chart Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("X-axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.bar(data_frame=df, x=x_values, y=y_values, color=x_values, title=chart_title, width=width, height=height, template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Histogram
if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("X-axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.histogram(data_frame=df, x=x_values, y=y_values, color=x_values, title=chart_title, width=width, height=height, template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Mapbox
# Create mapbox account (needs token)
if chart_select == 'Mapbox':
    st.sidebar.subheader("Mapbox Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        lat = st.sidebar.selectbox("Latitude", options=numeric_columns)
        lon = st.sidebar.selectbox("Longitude", options=numeric_columns)
        num_range = st.sidebar.selectbox("Range", options=numeric_columns)
        size = st.sidebar.selectbox("Size", options=numeric_columns)
        plot = px.scatter_mapbox(data_frame=df, lat=lat, lon=lon, color=num_range, size=size,
                                 color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=1, title=chart_title)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")

# Geo Scatter Plot
if chart_select == 'Geo Scatter Plot':
    st.sidebar.subheader("Geo Scatter Plot Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        locations = st.sidebar.selectbox("Locations", options=numeric_columns)
        size = st.sidebar.selectbox("Node Size", options=numeric_columns)
        projection = st.sidebar.selectbox("Projection", options=["natural earth", "orthographic"])
        theme = st.sidebar.selectbox("Color Theme", options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.scatter_geo(data_frame=df, locations=locations, size=size, projection=projection, color=locations, title=chart_title, width=(int)(width), height=(int)(height), template=theme)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
# Pie Chart
if chart_select == 'Pie Chart':
    st.sidebar.subheader("Pie Chart Settings")
    try:
        chart_title = st.sidebar.text_input("Enter a chart title")
        x_values = st.sidebar.selectbox("Names", options=numeric_columns)
        y_values = st.sidebar.selectbox("Values", options=numeric_columns)
        theme = st.sidebar.selectbox("Color Theme",
                                     options=["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn",
                                              "simple_white"])
        width = int(st.sidebar.text_input("Chart width", "700"))
        height = int(st.sidebar.text_input("Chart height", "700"))
        plot = px.pie(df, values=y_values, names=x_values, title=chart_title, template=theme, width=width, height=height)
        # Displaying the chart
        st.plotly_chart(plot, use_container_width=True)
    except Exception as e:
        print(f"{datetime.now()} - ERROR: {e}")
