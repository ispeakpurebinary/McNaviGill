# pip install folium
# pip install requests
# pip install selenium
# pip install datetime

import datetime
import folium
import requests
from selenium import webdriver
import time

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state

    except:
        print("Internet Not available")
        exit()
        return False


def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print(f"You Are in {city}, {state}")
        print(f"Your latitude = {lat} and longitude = {long}")
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = f"C:/screengfg/Location{datetime.date.today()}.html"

        obj.save(fileName)

        return fileName

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":

    print("---------------GPS Using Python---------------\n")

    page = gps_locator()
    if page:
        print("\nOpening File.............")
        dr = webdriver.Chrome()
        dr.get(page)
        time.sleep(4)
        dr.quit()
        print("\nBrowser Closed..............")
    else:
        print("Failed to generate location map.")

