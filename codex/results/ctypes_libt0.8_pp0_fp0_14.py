import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("NASA Propulsion and Rocket Equations")

# import all the additional needed libraries
from sys import argv
import requests
import lxml.html
import webbrowser

# define a function to find the mass of the rocket
def massRocket(dryMass, fuelMass, Isp):
    return dryMass + fuelMass

# define a function to find the thrust
def Thrust(thrustVac, thrustSL, Isp, atmPressure, atmTemp, atmLiquidTemp, g, atmDensityFactor):
    return (thrustVac * (atmPressure / 101.325) * ((atmTemp / atmLiquidTemp)**(g / (Isp * atmDensityFactor))))

# define a function to find the drag
def Drag(rocketDiameter, rocketArea, atmDensity, relativeVelocity):
    return (0.5 * atmDensity * relativeVelocity**2 * rocketArea)

# define a function to find the total mass
def TotalMass(rocketMass, fuelMass):
    return rocketMass + fuelMass
