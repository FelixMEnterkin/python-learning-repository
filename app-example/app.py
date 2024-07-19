import streamlit as st
 
import pandas as pd
import plotly.express as px
 
##################### Utility functions ###############################
def age_check(dob):
    today = pd.to_datetime('today')
 
    if dob + pd.DateOffset(years=6) > today:
        return '0-5 years'
    elif dob + pd.DateOffset(years=12) > today:
        return '6-11 years'
    elif dob + pd.DateOffset(years=18) > today:
        return '12-17 years'
    else:
        return '18+ years'
 
def data_cleaner(df):
    df['SEX'] = df['SEX'].map({1:'Male',
                               2:'Female'})
   
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')
 
    df['AGE RANGE'] = df['DOB'].apply(age_check)
 
    df.drop(['CHILD', 'DOB', 'UPN', 'MOTHER', 'MC_DOB'], axis=1, inplace=True)
 
    return df
 
##################### Plot functions ###################################

def gender_plot(df):
    fig = px.histogram(df,
                       x='SEX',
                       title='903 cohort breakdown via sex',
                       labels={'SEX':'Sex'})
    return fig 
 
 
 
 
 
##################### Main app code ###################################
st.title('903 Header Analysis Tool')
 
file = st.file_uploader('Please upload 903 header for analysis')
 
if file:
    unclean_df = pd.read_csv(file)
 
    df = data_cleaner(unclean_df)
 
 
 
    st.dataframe(df)
 