print("**************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

#Function that lists Gas Levels,randomly choosing one and returing it value
def gaslevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tanks","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Levels,randomly choosing one and returing it value
def listofgasstations():
    gasStations= ["Shell","Speedway","Marathon","Cicle k","Mobil","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


print(gaslevelGauge())
print(listofgasstations())
