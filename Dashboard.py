import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('hour.csv')

# Map season values
data['season'] = data['season'].replace({1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'})

# Map weathersit values
data['weathersit'] = data['weathersit'].replace({1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
                                               2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                                               3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                                               4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'})

# Map yr values
data['yr'] = data['yr'] + 2010 # add 2010 to yr values

# Map mnth values
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
data['mnth'] = data['mnth'].replace(range(1, 13), months)

# Map weekday values
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
data['weekday'] = data['weekday'].replace(range(0, 7), days)

# Filter data by season and weather situation
season = st.sidebar.selectbox('Select season', ['springer', 'summer', 'fall', 'winter'])
weathersit = st.sidebar.selectbox('Select weather situation', ['Clear, Few clouds, Partly cloudy, Partly cloudy',
                                                             'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                                                             'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                                                             'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'])
data = data[(data['season'] == season) & (data['weathersit'] == weathersit)]

# Calculate total rental bikes, casual users, and registered users
total_cnt = data['cnt'].sum()
total_casual = data['casual'].sum()
total_registered = data['registered'].sum()

# Display total rental bikes, casual users, and registered users
st.title('Dashboard Bikeshare Dataset')


# Display total rental bikes, casual users, and registered users using st.columns() and st.metric()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Rides", value=total_cnt)
with col2:
    st.metric("Total Casual Rides", value=total_casual)
with col3:
    st.metric("Total Registered Rides", value=total_registered)

# Calculate total rental bikes by month
monthly_rentals = data.groupby('mnth')['cnt'].sum().reset_index()

# Create horizontal bar chart for month
fig, ax = plt.subplots()
ax.barh(monthly_rentals['mnth'], monthly_rentals['cnt'])
ax.set_xlabel('Total rental bikes')
ax.set_title('Total rental bikes by month')
st.pyplot(fig)


# Calculate rental bikes by year
yearly_rentals = data.groupby('yr')['cnt'].sum().reset_index()

# Create pie chart for year
fig, ax = plt.subplots()
ax.pie(yearly_rentals['cnt'], labels=[str(year) for year in yearly_rentals['yr']])
ax.set_title('Total rental bikes by year')
st.pyplot(fig)

# Calculate rental bikes by weekday
daily_rentals = data.groupby('weekday')['cnt'].sum().reset_index()

daily_rentals['weekday'] = daily_rentals['weekday'].astype('category')
daily_rentals['weekday'] = daily_rentals['weekday'].cat.reorder_categories(days, ordered=True)

# Create line plot for weekday
fig, ax = plt.subplots()
ax.plot(daily_rentals['weekday'], daily_rentals['cnt'])
ax.set_xlabel('Weekday')
ax.set_ylabel('Total rental bikes')
ax.set_title('Total rental bikes by weekday')
st.pyplot(fig)

# Display some data
st.write(data.head())