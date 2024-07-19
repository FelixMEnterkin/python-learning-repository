''' 
To buid an app in python we can use sf-nova in vs code that allows us to complie an app and publish it to browser.
This will use the streamlit packedge that takes the python code and coverts it to java and html so that it can run - all 
we have to do is the python code.



    we can run our apps in codespace that means we dont have to properly publish on the web.
    because we are running this locally on out computer we can use sensistive data
    sf-nova is teh extention that allows us to test  our apps built by social finance 
    this then appeas at the bottom of our left hand pane, giving us an option to launce a preview 


To buid the app we have to create three files, a py script that contains the app code, a requirments document that includes 
the downloads for any non-standard python libaraies we need, and the index.html file that complies the app.

This here is the script file that contains the code for the app. It is sub divided into utility functions and the main app.


stramlit contains all the pre built front end elemts we need to format the website, it translates the python code to java and html. 
Look up the streamlit documentation to build stuff together. Once you understand langages you can simply read the documentation
When you launch the preview, you must be on the relevent py file at the time

'''

import streamlit as st
 
import pandas as pd
import plotly.express as px
 

# Utility functions
''' 
There are a number of functions that we want our app to perform and it is easiest to define these as functios beforehand 
and then call them within a  master function that can be used in the app code.
'''


def age_bucket(dob_dt):
    today = pd.to_datetime('today')
 
    if dob_dt + pd.DateOffset(years=6) > today:  
        return '0-5 years'
    elif dob_dt + pd.DateOffset(years=12) > today:
        return '6-11 years'
    elif dob_dt + pd.DateOffset(years=18) > today:
        return '12-17 years'
    else:
        return '18+ years old'
    
# create one master function for data clean    
 
def ingress(df):
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
 
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')
 
    df['Age range'] = df['DOB'].apply(age_bucket)
 
    df.drop(['CHILD', 'UPN', 'MOTHER', 'MC_DOB'], axis=1, inplace=True)
 
    return df
 
# Plot functions
def gender_plot(df):
    fig = px.histogram(df,
                       'SEX',
                       title='903 gender breakdown')
    return fig
 
def age_pie(df):
    fig = px.pie(df,
                 names='Age range',
                 title='903 age breakdown')
    return fig
 




# Main app code
''' 
This code actually compiles the app itself. There are not that many lines of code here as the majority of tasks can be defined in functions and 
included within the data clean ingress.

The eaxct functions that are part of the streamlit library can be found by searching streamlit api. This allows the python code to be translated
the java and html code that the browser works with. Browesers all run using Java. 

    Browsers also run localy on our computer

The app itself for the most part is incuded within an if statement that tests if data has been inpout. the syntax `if file != None:` would acheive
the save thing. Everything else is within this if statement so it ponly runs with data. 

'''

st.title('903 header analysis')
 
file = st.file_uploader('Drag and drop 903 header file here')

if file:
    unclean_df = pd.read_csv(file)
 
    df = ingress(unclean_df)
 
 
    chosen_ethnicities = st.sidebar.multiselect('Select ethncities to view breakdowns by:',
                                        list(df['ETHNIC'].unique()),
                                        list(df['ETHNIC'].unique()))
   
    df = df[df['ETHNIC'].isin(chosen_ethnicities)]
 
    st.dataframe(df)
 
    gender_plot_fig = gender_plot(df)
    st.plotly_chart(gender_plot_fig)
 
    age_plot_fig = age_pie(df)
    st.plotly_chart(age_plot_fig)
 

 ''''
 The index html is a file that every website has that specifies how the website appears
 we can includfe our python code in the file
 
 '''