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

temp_max_min(46.2389, 14.3556)

def raz_dne_no(lat, lon):