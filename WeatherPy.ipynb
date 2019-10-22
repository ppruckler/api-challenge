{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WeatherPy\n",
    "----\n",
    "\n",
    "#### Note\n",
    "* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step complete!\n"
     ]
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "from pprint import pprint\n",
    "\n",
    "# Import API key\n",
    "from api_keys import api_key\n",
    "apikey = f'&APPID={api_key}'\n",
    "\n",
    "\n",
    "#base url for API call\n",
    "url = 'http://api.openweathermap.org/data/2.5/weather?q='\n",
    "\n",
    "# Incorporated citipy to determine city based on latitude and longitude\n",
    "from citipy import citipy\n",
    "\n",
    "# Output File (CSV)\n",
    "output_data_file = \"cities.csv\"\n",
    "\n",
    "# Range of latitudes and longitudes\n",
    "lat_range = (-90, 90)\n",
    "lng_range = (-180, 180)\n",
    "print(\"Step complete!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate Cities List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List for holding lat_lngs and cities\n",
    "lat_lngs = []\n",
    "cities = []\n",
    "\n",
    "# Create a set of random lat and lng combinations\n",
    "lats = np.random.uniform(low=-90.000, high=90.000, size=1500)\n",
    "lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)\n",
    "lat_lngs = zip(lats, lngs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step complete! You collected lat/long info for 621 cities.\n"
     ]
    }
   ],
   "source": [
    "# Identify nearest city for each lat, lng combination\n",
    "for lat_lng in lat_lngs:\n",
    "    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name\n",
    "    \n",
    "    # If the city is unique, then add it to a our cities list\n",
    "    if city not in cities:\n",
    "        cities.append(city)\n",
    "\n",
    "# Print the city count to confirm sufficient count\n",
    "len(cities)\n",
    "print(f\"Step complete! You collected lat/long info for {len(cities)} cities.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Perform API Calls\n",
    "* Perform a weather check on each city using a series of successive API calls.\n",
    "* Include a print log of each city as it'sbeing processed (with the city number and city name).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processing Record 1 of Set 1 | rikitea\n",
      "Processing Record 2 of Set 1 | namibe\n",
      "Processing Record 3 of Set 1 | isangel\n",
      "Processing Record 4 of Set 1 | shahe\n",
      "Processing Record 5 of Set 1 | albany\n",
      "Processing Record 6 of Set 1 | busselton\n",
      "Processing Record 7 of Set 1 | camacha\n",
      "Processing Record 8 of Set 1 | dikson\n",
      "Processing Record 9 of Set 1 | tuktoyaktuk\n",
      "Processing Record 10 of Set 1 | saskylakh\n",
      "Processing Record 11 of Set 1 | constitucion\n",
      "Processing Record 12 of Set 1 | moree\n",
      "Processing Record 13 of Set 1 | hofn\n",
      "Processing Record 14 of Set 1 | butaritari\n",
      "Processing Record 15 of Set 1 | arraial do cabo\n",
      "Processing Record 16 of Set 1 | lusambo\n",
      "Processing Record 17 of Set 1 | spirit river\n",
      "Processing Record 18 of Set 1 | marienburg\n",
      "Processing Record 19 of Set 1 | sao filipe\n",
      "Processing Record 20 of Set 1 | vaini\n",
      "Processing Record 21 of Set 1 | nangong\n",
      "Processing Record 22 of Set 1 | goundam\n",
      "Processing Record 23 of Set 1 | ushuaia\n",
      "City not found. Skipping...\n",
      "Processing Record 24 of Set 1 | jackson\n",
      "Processing Record 25 of Set 1 | jonkoping\n",
      "Processing Record 26 of Set 1 | carnarvon\n",
      "Processing Record 27 of Set 1 | acobamba\n",
      "Processing Record 28 of Set 1 | port alfred\n",
      "Processing Record 29 of Set 1 | fare\n",
      "Processing Record 30 of Set 1 | yellowknife\n",
      "Processing Record 31 of Set 1 | barrow\n",
      "Processing Record 32 of Set 1 | boguchany\n",
      "City not found. Skipping...\n",
      "Processing Record 33 of Set 1 | luderitz\n",
      "Processing Record 34 of Set 1 | inuvik\n",
      "Processing Record 35 of Set 1 | pevek\n",
      "Processing Record 36 of Set 1 | punta arenas\n",
      "Processing Record 37 of Set 1 | champerico\n",
      "Processing Record 38 of Set 1 | cape town\n",
      "City not found. Skipping...\n",
      "Processing Record 39 of Set 1 | nishihara\n"
     ]
    }
   ],
   "source": [
    "#Create lists for the DF\n",
    "New_Cities = []\n",
    "Clouds = []\n",
    "Dates = []\n",
    "Humidities = []\n",
    "Latitudes = []\n",
    "Longitudes = []\n",
    "Max_Temps = []\n",
    "Wind_Speeds = []\n",
    "Countries = []\n",
    "\n",
    "#Set Counters\n",
    "count_one = 0\n",
    "set_one = 1\n",
    "\n",
    "#Loops through to make DF columns & logger\n",
    "for city in cities:\n",
    "    try:\n",
    "        response = requests.get(url + city + apikey).json()\n",
    "        Clouds.append(response['clouds']['all'])\n",
    "        Countries.append(response['sys']['country'])\n",
    "        Dates.append(response['dt'])\n",
    "        Humidities.append(response['main']['humidity'])\n",
    "        Latitudes.append(response['coord']['lat'])\n",
    "        Longitudes.append(response['coord']['lon'])\n",
    "        Max_Temps.append(response['main']['temp_max'])\n",
    "        Wind_Speeds.append(response['wind']['speed'])\n",
    "        \n",
    "        if count_one > 48:\n",
    "            count_one = 1\n",
    "            set_one += 1\n",
    "            New_Cities.append(city)\n",
    "        else:\n",
    "            count_one += 1\n",
    "            New_Cities.append(city)\n",
    "        print(f\"Processing Record {count_one} of Set {set_one} | {city}\")\n",
    "    except Exception:\n",
    "        print(\"City not found. Skipping...\")\n",
    "\n",
    "print(\"------------------------------\")\n",
    "print(\"Data Retrieval Complete\")\n",
    "print(\"------------------------------\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert Raw Data to DataFrame\n",
    "* Export the city data into a .csv.\n",
    "* Display the DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the DF\n",
    "WeatherDF = pd.DataFrame({'City': New_Cities,\n",
    "                          'Cloudiness': Clouds,\n",
    "                          'Country': Countries,\n",
    "                          'Date' : Dates,\n",
    "                          'Humidity': Humidities,\n",
    "                          'Lat': Latitudes,'Lng': Longitudes,\n",
    "                          'Max Temp': Max_Temps,\n",
    "                          'Wind Speed': Wind_Speeds})\n",
    "\n",
    "# Preview DF\n",
    "WeatherDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert temps to Fahrenheit\n",
    "WeatherDF['Max Temp'] = (9 / 5) * (WeatherDF['Max Temp'] - 273) + 32\n",
    "\n",
    "# Preview DF\n",
    "WeatherDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print output data to csv\n",
    "WeatherDF.to_csv(output_data_file, index_label= 'City_ID')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Plotting the Data\n",
    "* Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.\n",
    "* Save the plotted figures as .pngs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Temperature Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.scatter(WeatherDF[\"Lat\"], WeatherDF[\"Max Temp\"], edgecolors=\"black\")\n",
    "plt.title(f\"City Latitude vs. Max Temperature ({time.strftime('%x')})\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.ylabel(\"Max Temperature (F)\")\n",
    "plt.grid (b=True, linestyle=\"-\", color=\"lightgrey\")\n",
    "plt.savefig(\"Latitude vs Temperature.png\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Humidity Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.scatter(WeatherDF[\"Lat\"], WeatherDF[\"Humidity\"], edgecolors=\"black\")\n",
    "plt.title(f\"City Latitude vs. Humidity ({time.strftime('%x')})\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.ylabel(\"Humidity (%)\")\n",
    "plt.ylim(15, 105)\n",
    "plt.grid (b=True, linestyle=\"-\", color=\"lightgrey\")\n",
    "plt.savefig(\"Latitude vs Humidity.png\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Cloudiness Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.scatter(WeatherDF[\"Lat\"], WeatherDF[\"Cloudiness\"], edgecolors=\"black\")\n",
    "plt.title(f\"City Latitude vs. Cloudiness ({time.strftime('%x')})\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.ylabel(\"Cloudiness (%)\")\n",
    "plt.grid (b=True, linestyle=\"-\", color=\"lightgrey\")\n",
    "plt.savefig(\"Latitude vs Cloudiness.png\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Wind Speed Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.scatter(WeatherDF[\"Lat\"], WeatherDF[\"Wind Speed\"], edgecolors=\"black\")\n",
    "plt.title(f\"City Latitude vs. Wind Speed ({time.strftime('%x')})\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.ylabel(\"Wind Speed (mph)\")\n",
    "plt.ylim(-2, 34)\n",
    "plt.grid (b=True, linestyle=\"-\", color=\"lightgrey\")\n",
    "plt.savefig(\"Latitude vs WindSpeed.png\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernel_info": {
   "name": "python3"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "nteract": {
   "version": "0.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
