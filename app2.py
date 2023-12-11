import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# Get the current script directory
current_directory = Path(__file__).resolve().parent

# Define the relative path to the CSV file
# Use forward slashes to maintain compatibility across platforms
file_path = current_directory / 'cause_of_deaths.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Sidebar - Country/Territory Dropdown
selected_country = st.sidebar.selectbox('Select Country/Territory:', df['Country/Territory'].unique())

# Sidebar - Year Dropdown
selected_year = st.sidebar.selectbox('Select Year:', df['Year'].unique())

# Sidebar - Diseases Dropdown
disease_columns = df.columns[3:]
selected_disease = st.sidebar.selectbox('Select Disease:', disease_columns)

# Filter data based on user selection
filtered_data = df[(df['Country/Territory'] == selected_country) & (df['Year'] == selected_year)]

# Display table for the selected Country/Territory
st.write(f"### Data for {selected_country} in {selected_year}")
st.write(filtered_data)

# Line chart for selected Disease over the years
line_chart_data = df[df['Country/Territory'] == selected_country]
line_chart_data = line_chart_data.set_index('Year')[[selected_disease]]
st.write(f"### Line Chart for {selected_disease} in {selected_country}")
st.line_chart(line_chart_data)

# Bar chart for selected Disease
bar_chart_data = df.groupby('Country/Territory')[selected_disease].sum().reset_index()
bar_chart_data = bar_chart_data[bar_chart_data[selected_disease] > 0]  # Exclude countries with 0 deaths
st.write(f"### Bar Chart for Total {selected_disease} by Country")
fig_bar = px.bar(bar_chart_data, x='Country/Territory', y=selected_disease, title=f'Total {selected_disease} by Country')
st.plotly_chart(fig_bar)

# Pie chart for selected Disease (Top 10 Countries)
top10_pie_chart_data = df.groupby('Country/Territory')[selected_disease].sum().reset_index()
top10_pie_chart_data = top10_pie_chart_data[top10_pie_chart_data[selected_disease] > 0]  # Exclude countries with 0 deaths
top10_pie_chart_data = top10_pie_chart_data.sort_values(by=selected_disease, ascending=False).head(10)
st.write(f"### Pie Chart for Top 10 {selected_disease} Distribution by Country")
fig_top10_pie = px.pie(top10_pie_chart_data, 
                       values=selected_disease, 
                       names='Country/Territory', 
                       title=f'Top 10 {selected_disease} Distribution by Country',
                       labels={'Country/Territory': 'Country', selected_disease: 'Total Deaths'},
                       hole=0.3)  # Adjust the hole size for better readability
st.plotly_chart(fig_top10_pie)
