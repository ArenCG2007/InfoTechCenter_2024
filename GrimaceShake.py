print("\n**********************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def Weather():
    weatherForecast = ["snowy","blizzard","rainy","foggy","windy","icy","sunny",""]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable t ocall the Weather() once VRS(Vehicle Response System) is determined
weatherAlert = Weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged allowing a max speed of 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep (1.5)
        print("VRS has been engaged allowing a max speed of 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged allowing a max speed of 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged allowing a max speed of 75mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 15 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged allowing a max speed of 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged allowing a max speed of 40mph")
    else:
        print("\nNational Weather Service has a forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged.")




vehicleResponseSystem()