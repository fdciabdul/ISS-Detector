## Code by Abdul Muttaqin

import requests
import json
from math import sqrt
import time

def iss_position():
    data_iss = requests.get("http://api.open-notify.org/iss-now.json")
    data_iss = data_iss.json()
    print("Garis Lintang ( Latitude ) ISS : ", data_iss["iss_position"]["latitude"])
    print("Garis Bujur ( Longitude ) ISS : ", data_iss["iss_position"]["longitude"])
    return (data_iss["iss_position"]["latitude"], data_iss["iss_position"]["longitude"])

def computer_position():
    data_pos = requests.get("http://ip-api.com/json/")
    data_pos = data_pos.json()
    print("Lokasimu Sekarang : ", data_pos["city"], "\n")
    print("Posisi Garis Lintang: ", data_pos["lat"])
    print("Posisi Garis Bujur: ", data_pos["lon"])
    print("\n======================\n")
    return (data_pos["lat"], data_pos["lon"])

def calc_visiblity_area(xa, ya, xb, yb):
    return (round(sqrt((xb - xa)**2 + (yb - ya)**2), 4))

if (__name__ == '__main__'):
    xa, ya = computer_position()
    while 1:
        xb, yb = iss_position()
        distance = calc_visiblity_area(float(xa), float(ya), float(xb), float(yb))
        if (distance <= 33):
            print("\n\033[0;37;42mISS ADA DI ATAS LANGIT KOTAMU:)\033[0;37;48m")
        else:
            print("\n\033[0;37;41mISS TAK ADA DIATAS KOTAMU :(\033[0;37;48m")
        print("Jarak mu dengan ISS Adalah : ", distance, "\n")
        time.sleep(2)