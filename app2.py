import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Load the dataset
# Use double backslashes or a raw string for Windows paths
# Example with double backslashes:
# file_path = 'C:\\Users\\Saman\\Desktop\\phyton_ws\\Deaths Worldwide\\cause_of_deaths.csv'
# Example with a raw string:
file_path = r'C:\Users\Saman\Desktop\phyton_ws\Deaths Worldwide\cause_of_deaths.csv'

# Alternatively, if you are running this on a non-Windows system, use a Unix-style path:
# file_path = '/path/to/cause_of_deaths.csv'

df = pd.read_csv(file_path)

# Rest of the code remains unchanged
