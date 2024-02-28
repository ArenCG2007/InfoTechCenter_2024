


#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome Branch Starts Here
timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")


# Gasoline Branch Starts Here
print("**************************************************")
print("\nGasoline Branch\n\n")

#Function that lists Gas Levels,randomly choosing one and returing it value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations,randomly choosing one and returing it value
def listOfGasStations():
    gasStations= ["Shell","Speedway","Marathon","Cicle k","Mobil","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then locate a nearby gas station
#by calling thw ListOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print("    ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low,checking Google Maps for the nearest gas station")
        sleep(2.5)
        print("The closest gas station is ",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank")
        sleep(2.5)
        print("The closest gas station is ",listOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is at half tank,plenty to reach your destination")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full")
        

gasLevelAlert()
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

