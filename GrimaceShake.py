print("**************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

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
