import requests
""""
def trenutna_temp(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max"
    call = requests.get(base_url).json()
    print(call ["daily"] ["temperature_2m_max"])

trenutna_temp(45.12, 14.5)
"""


def temp_max_min(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(base_url).json()
    print(call ["daily"] ["temperature_2m_max"])
    print(call ["daily"] ["temperature_2m_min"])
    print(call ["daily"] ["time"])

#temp_max_min(46.2389, 14.3556)

def raz_dne_no(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(base_url).json()
    razlika = 0
    for i in range(len(call ["daily"]["time"])):
        dnevna = call["daily"] ["temperature_2m_max"]
        nocna = call ["daily"] ["temperature_2m_min"]
        razlika = dnevna[i] - nocna[i]
    print(razlika)
raz_dne_no(46.2389, 14.3556)


def trenutna_temp2(lat, lon):           #bolsi nacin kako se pise url
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : "lat",
              "longitude" : "lon", 
              "current" : "temperature_2m_max", 
              "timezone" : "auto", 
              "forecast_days" : 1
              }
    call = requests.get(base_url, params=params)
    json = call.json()
    return json["current"] ["temperature_2m"]
#trenutna_temp2(46.2389, 14.3556)


def min_max_temp(lat, lon): 
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat,
              "longitude" : lon, 
              "daily" : "temperature_2m_max,temperature_2m_min", 
              "forecast_days" : 1
              } 
    call = requests.get(base_url, params=params)
    json = call.json()
    return json["daily"] ["temperature_2m_max"], json ["daily"] ["temperature_2m_min"]
cities = [
    ("Ljubljana", 46.0511, 14.5051), 
    ("Maribor", 46.5558, 15.6459),
    ("Celje", 46.2309, 15.2604),
    ("Kranj", 46.2389, 14.3556),
]
for c in cities:
    print(min_max_temp (c[1],c[2]),c[0])