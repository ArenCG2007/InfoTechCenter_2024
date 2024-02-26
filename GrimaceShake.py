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
        print("VRS has been engaged allowing a max speed of 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged allowing a max speed of 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged allowing a max speed of 60mph")



vehicleResponseSystem()