import pymysql
import streamlit as st
import pandas as pd

# Title
st.video("C:/Users/Deepa/Downloads/How to book bus tickets online _ redBus _ Online Bus Ticket Booking (1).mp4")
st.markdown("""
# REDBUS
### *Create your own bus booking as easy as A B C*
""")

# Connect to the SQL database
myconnection = pymysql.connect(
    host="localhost",
    user="root",
    password="Reethikasql11",
    database="bus_routes"
)

try:
    # Fetch all data from the 'buses' table
    query = "SELECT * FROM buses"
    df = pd.read_sql(query, myconnection)

    # Fetch unique route names
    routes = df['route_name'].unique().tolist()

    # Sidebar for selecting route names
    selected_route = st.sidebar.selectbox('Select Route', [None] + routes)

    # Filter DataFrame based on selected route to get related bus names
    if selected_route:
        route_filtered_df = df[df['route_name'] == selected_route]
        bus_names = route_filtered_df['bus_name'].unique().tolist()
    else:
        bus_names = []

    # Sidebar filter for bus names
    selected_bus_name = st.sidebar.selectbox('Select Bus Name', [None] + bus_names)

    # Apply filter to the DataFrame
    filtered_df = df.copy()
    if selected_route:
        filtered_df = filtered_df[filtered_df['route_name'] == selected_route]
    if selected_bus_name:
        filtered_df = filtered_df[filtered_df['bus_name'] == selected_bus_name]

    # Display the filtered data
    st.write(filtered_df)

finally:
    # Close the database connection
    myconnection.close()


    # Add a website link to the bottom-right corner using st.write
st.write(
    "[Visit Our Website](https://www.redbus.in/)",
    unsafe_allow_html=True
)
# Home button
if st.button('Home'):
    st.session_state.page = 'home'

# Project details
if 'page' in st.session_state and st.session_state.page == 'home':
    st.markdown("""
    ## Project Title
    #### Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
    #### Skills take away From This Project - Web Scraping using Selenium, Python, Streamlit , SQL
    **Featuers in this App:**
    - **Select a route**: Choose from various bus routes.
    - **Select a bus name**: Filter by specific bus names.
    - **View filtered data**: Display bus details based on selected filters.
    
    **Features**
    - Interactive filters
    - Real-time data fetching from a SQL database
    - User-friendly interface
    
    For more information, visit our [website](https://example.com).
    """)