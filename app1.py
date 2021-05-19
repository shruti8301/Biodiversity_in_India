import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import plotly.graph_objs as go
from PIL import Image
image = Image.open('Frame 1.png')
st.image(image)
st.markdown("<h1 style='text-align: center; color: #8DFF99;'>Biodiversity of Species in India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left;'>There are more than 45000 species of plants and 91000 species of animals in India, accounting for about 8% of all recorded species in the world. Having 4 biodiversity hotspots, our country is very biodiverse in nature. As the role of biodiversity in species plays a major role in boosting the productivity of our ecosystem and has social benefits such as cultural and recreational values, it is crucial to address the gradually declining biodiversity as all species are heavily interdependent on each other. This website is dedicated to observing the biodiversity of species in India and using data visualization techniques to identify the vital elements in it.</p>", unsafe_allow_html=True)
#st.title('Biodiversity of Species in India')
@st.cache
def load_data(nrows):
    data = pd.read_csv(r'species.csv',nrows=nrows)
    return data
#data_load_state = st.text('Loading data...')

species_data = load_data(40).set_index('Common_Name')
g_data = load_data(106)
st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Species Dataset</b></h3>", unsafe_allow_html=True)
st.write(g_data)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.markdown("<h3 style='text-align: left; color: #FFFFFF; font-family:'Lato'; '><b>The dashboard will help a researcher to get to know more about the given datasets and it's output.</b></h3>", unsafe_allow_html=True)

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

data = pd.read_csv(r'species.csv')


chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis by Biodiversity", True, key = 1)
selected_status = st.sidebar.selectbox('Select the Option:',
                                       options = ['Status',
                                                  'Kingdom', 'State_Found',
                                                  'Class'])

fig = go.Figure()
st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Visual Charts with index set as Common Name of Species</b></h3>", unsafe_allow_html=True)
if chart_visual == 'Line Chart':
    if selected_status == 'Status':
        fig.add_trace(go.Scatter(x = data.Common_Name, y = data.Status,
                                 mode = 'lines',
                                 name = 'Status',
				 line = dict(color='#EFA35E')))

    if selected_status == 'Kingdom':
        fig.add_trace(go.Scatter(x = data.Common_Name, y = data.Kingdom,
                                 mode = 'lines', name = 'Kingdom',line=dict(color='#EA456D')))
    if selected_status == 'State_Found':
        fig.add_trace(go.Scatter(x = data.Common_Name, y = data.State_Found,
                                 mode = 'lines',
                                 name = 'State_Found',line=dict(color='#EAD945')))
    if selected_status == 'Class':
        fig.add_trace(go.Scatter(x=data.Common_Name, y=data.Class,
                                 mode='lines',
                                 name="Class",line=dict(color='#EAB245')))

elif chart_visual == 'Bar Chart':
    if selected_status == 'Status':
        fig.add_trace(go.Bar(x=data.Common_Name, y=data.Status,
                             name='Status',marker_color='#CEE254'))
    if selected_status == 'Kingdom':
        fig.add_trace(go.Bar(x=data.Common_Name, y=data.Kingdom,
                             name='Kingdom',marker_color='#FB6592'))
    if selected_status == 'State_Found':
        fig.add_trace(go.Bar(x=data.Common_Name, y=data.State_Found,
                             name='State_Found',marker_color='#FF9776'))
    if selected_status == 'Class':
        fig.add_trace(go.Bar(x=data.Common_Name, y=data.Class,
                             name="Class",marker_color='#9CFB8C'))

elif chart_visual == 'Bubble Chart':
    if selected_status == 'Status':
        fig.add_trace(go.Scatter(x=data.Common_Name,
                                 y=data.Status,
                                 mode='markers',
                                 marker=dict(size=16,color=np.random.randn(500),colorscale='Viridis',showscale=True),
                                 name='Status'))

    if selected_status == 'Kingdom':
        fig.add_trace(go.Scatter(x=data.Common_Name, y=data.Kingdom,
                                 mode='markers',
                                 marker=dict(size=16,color=np.random.randn(500),colorscale='Viridis',showscale=True),
                                 name='Kingdom'))

    if selected_status == 'State_Found':
        fig.add_trace(go.Scatter(x=data.Common_Name,
                                 y=data.State_Found,
                                 mode='markers',
                                 marker=dict(size=16,color=np.random.randn(500),colorscale='Viridis',showscale=True),
                                 name = 'State_Found'))
    if selected_status == 'Class':
        fig.add_trace(go.Scatter(x=data.Common_Name,
                                 y=data.Class,
                                 mode='markers',
                                 marker=dict(size=16,color=np.random.randn(500),colorscale='Viridis',showscale=True),
                                 name="Class"))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)


st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Bar Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the percentage of species in India</p>", unsafe_allow_html=True)
#Bar Chart
st.bar_chart(species_data['Percentage'])
#Name=alt.Chart(species_data).mark_bar().encode(x='Common_Name',y='Number_in_India')
#st.write(Name)
line_data = load_data(30).set_index('Class')
#st.line_chart(line_data['Number_in_India'])
st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Bubble Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the ratio of species in India to species in World</p>", unsafe_allow_html=True)

data=[[0,2,0],
          [3,4,75],
          [3,3,100],
          [12,40,30],
          [12,50,24],
          [4,4,100],
          [50,250,20],
          [135,135,100],
          [600,700,85.71428571],
          [150,200,75],
          [70,88,79.54545455],
          [150,200,75],
          [325,325,100],
          [100,150,66.66666667],
          [100,200,50],
          [200,200,100],
          [210,210,100],
          [300,500,60],
          [350,1000,35],
          [500,70,71.42857143],
          [674,700,96.28571429],
          [15000,20000,75],
          [12000,14000,85.71428571],
          [90000,100000,90],
          [10000,14000,71.42857143],
          [8000,10000,80],
          [2145,4000,53.625],
          [3122,4220,73.98104265],
          [6000,10000,60],
          [25500,30000,85]]
df=pd.DataFrame (data, columns = ['India','World','Ratio'])
Ratio= alt.Chart(df).mark_circle().encode(x='India', y='World', size='Ratio', color='Ratio', tooltip=['India', 'World', 'Ratio']).interactive()
st.write(Ratio)


t_data=load_data(100)
n_data=load_data(100)


st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Area Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the Number of Species in India and World and their Percentage in India</p>", unsafe_allow_html=True)

s_data=load_data(20)
ds=pd.DataFrame(s_data, columns = ['Number_in_world','Percentage','Number_in_India'])
st.area_chart(ds)



#plt.hist(n_data["Kingdom"])
#plt.hist(n_data["Class"])
#plt.xlabel("Kingdom & Class")
#plt.ylabel("Values")
#plt.legend(labels=["Kingdom","Class"])

st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot()

st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Scatter Plot</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the IUCN Status of Species with their precentage in India</p>", unsafe_allow_html=True)

fig = px.scatter(t_data, x=t_data['Common_Name'], y=t_data['Status'], color=t_data['Percentage'])
fig.update_yaxes(showgrid=False)
fig.update_xaxes(showgrid=False)
st.plotly_chart(fig)



st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Pie Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the Class of Species with number of species in India</p>", unsafe_allow_html=True)

fig1 = px.pie(t_data, values=t_data['Number_in_India'], names=t_data['Class'])
st.plotly_chart(fig1)
st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Histogram</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the count of catergories of IUCN status of Species</p>", unsafe_allow_html=True)

fig = px.histogram(t_data['Status'])
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig)
st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Bar Plot</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the species with the states they are found in with respect to their percentage in India</p>", unsafe_allow_html=True)

fig = px.bar_polar(t_data, r=t_data['Common_Name'], theta=t_data['State_Found'], color=t_data['Percentage'],
                   color_discrete_sequence= px.colors.sequential.Plasma)
fig.update_polars(bgcolor='#0e1117')
fig.update_xaxes(gridcolor='#32353a')
st.plotly_chart(fig)

st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Stacked Bar Plot</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the IUCN status of species with their Percentage in India and the State they are found in</p>", unsafe_allow_html=True)

fig5 = px.bar(t_data, x="State_Found", y="Percentage", color="Status")
fig5.update_yaxes(showgrid=False)
st.plotly_chart(fig5)

st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Pie Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the division of population of species in India based on the types of kingdom</p>", unsafe_allow_html=True)

fig1 = px.pie(t_data, values=t_data['Number_in_India'], names=t_data['Kingdom'])
st.plotly_chart(fig1)
st.markdown("<h3 style='text-align: left; color: #9BFB6E;'><b>Chloropleth Map</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the number of species in each state in the map of India using a color plot</p>", unsafe_allow_html=True)


import pandas as pd
import plotly.express as px

df = pd.read_csv(r'state .csv')

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='value',
    color_continuous_scale='Viridis'
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
st.plotly_chart(fig)

st.markdown("<h3 style='text-align: left; color: #F9CD5D;'><b>Point Chart</b></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: #FFFFFF;'>To visualize the Kingdom and Class of species with respect to Status of species</p>", unsafe_allow_html=True)
de=pd.DataFrame(n_data, columns = ['Class','Kingdom','Status','Percentage'])

Percentage= alt.Chart(de).mark_point().encode(x='Class', y='Kingdom', size='Status', color='Status', tooltip=['Class', 'Kingdom', 'Status']).interactive()
st.write(Percentage)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
