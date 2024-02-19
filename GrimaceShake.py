print("**************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random


def gaslevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tanks","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel




print(gaslevelGauge())