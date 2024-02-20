print("**************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

#Function that lists Gas Levels,randomly choosing one and returing it value
def gaslevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tanks","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations,randomly choosing one and returing it value
def listofgasStations():
    gasStations= ["Shell","Speedway","Marathon","Cicle k","Mobil","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then locate a nearby gas station
#by calling thw ListOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelGauge = gaslevelGauge()
    print(milesToGasStationsLow)
    print(milesToGasStationsQuarterTank)

gasLevelAlert()