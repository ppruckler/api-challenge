#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[13]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from pprint import pprint

# Import API key
from api_keys import api_key
apikey = f'&APPID={api_key}'


#base url for API call
url = 'http://api.openweathermap.org/data/2.5/weather?q='

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)
print("Step complete!")


# ## Generate Cities List

# In[14]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)


# In[15]:


# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)
print(f"Step complete! You collected lat/long info for {len(cities)} cities.")


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[ ]:


#Create lists for the DF
New_Cities = []
Clouds = []
Dates = []
Humidities = []
Latitudes = []
Longitudes = []
Max_Temps = []
Wind_Speeds = []
Countries = []

#Set Counters
count_one = 0
set_one = 1

#Loops through to make DF columns & logger
for city in cities:
    try:
        response = requests.get(url + city + apikey).json()
        Clouds.append(response['clouds']['all'])
        Countries.append(response['sys']['country'])
        Dates.append(response['dt'])
        Humidities.append(response['main']['humidity'])
        Latitudes.append(response['coord']['lat'])
        Longitudes.append(response['coord']['lon'])
        Max_Temps.append(response['main']['temp_max'])
        Wind_Speeds.append(response['wind']['speed'])
        
        if count_one > 48:
            count_one = 1
            set_one += 1
            New_Cities.append(city)
        else:
            count_one += 1
            New_Cities.append(city)
        print(f"Processing Record {count_one} of Set {set_one} | {city}")
    except Exception:
        print("City not found. Skipping...")

print("------------------------------")
print("Data Retrieval Complete")
print("------------------------------")


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[ ]:


# Create the DF
WeatherDF = pd.DataFrame({'City': New_Cities,
                          'Cloudiness': Clouds,
                          'Country': Countries,
                          'Date' : Dates,
                          'Humidity': Humidities,
                          'Lat': Latitudes,'Lng': Longitudes,
                          'Max Temp': Max_Temps,
                          'Wind Speed': Wind_Speeds})

# Preview DF
WeatherDF.head()


# In[ ]:


# Convert temps to Fahrenheit
WeatherDF['Max Temp'] = (9 / 5) * (WeatherDF['Max Temp'] - 273) + 32

# Preview DF
WeatherDF.head()


# In[ ]:


# Print output data to csv
WeatherDF.to_csv(output_data_file, index_label= 'City_ID')


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[ ]:


plt.scatter(WeatherDF["Lat"], WeatherDF["Max Temp"], edgecolors="black")
plt.title(f"City Latitude vs. Max Temperature ({time.strftime('%x')})")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")
plt.grid (b=True, linestyle="-", color="lightgrey")
plt.savefig("Latitude vs Temperature.png")
plt.show()


# #### Latitude vs. Humidity Plot

# In[ ]:


plt.scatter(WeatherDF["Lat"], WeatherDF["Humidity"], edgecolors="black")
plt.title(f"City Latitude vs. Humidity ({time.strftime('%x')})")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.ylim(15, 105)
plt.grid (b=True, linestyle="-", color="lightgrey")
plt.savefig("Latitude vs Humidity.png")
plt.show()


# #### Latitude vs. Cloudiness Plot

# In[ ]:


plt.scatter(WeatherDF["Lat"], WeatherDF["Cloudiness"], edgecolors="black")
plt.title(f"City Latitude vs. Cloudiness ({time.strftime('%x')})")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.grid (b=True, linestyle="-", color="lightgrey")
plt.savefig("Latitude vs Cloudiness.png")
plt.show()


# #### Latitude vs. Wind Speed Plot

# In[ ]:


plt.scatter(WeatherDF["Lat"], WeatherDF["Wind Speed"], edgecolors="black")
plt.title(f"City Latitude vs. Wind Speed ({time.strftime('%x')})")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.ylim(-2, 34)
plt.grid (b=True, linestyle="-", color="lightgrey")
plt.savefig("Latitude vs WindSpeed.png")
plt.show()


# In[ ]:




