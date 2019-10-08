#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment6
"""

class ConversionInputError(Exception):
    pass

def CelsiusToKelvin(cel):
    #function to convert Celsius to Kelvin to 2 decima points
    kel = float(cel) + 273.15
    return round(kel, 2)

def CelsiusToFahrenheit(cel):
    #function to convert Celsius to Fahrenheit to 2 decimal points
    fah = (float(cel) * 9/5) + 32
    return round(fah, 2)

def FahrenheitToCelsius(fah):
    #function to convert Fahrenheit to Celsiuc to 2 decimal points
    cel = (float(fah) - 32) * 5/9
    return round(cel, 2)

def FahrenheitToKelvin(fah):
    #function to convert Fahrenheit to Kelvin to 2 decimal points
    kel = (float(fah) + 459.67) * 5/9
    return round(kel, 2)

def KelvinToCelsius(kel):
    #function to convert Kelvin to Celsius to 2 decimal points
    cel = float(kel) - 273.15
    return round(cel, 2)

def KelvinToFahrenheit(kel):
    #function to convert Kelvin to Fahrenheit to 2 decimal points
    fah = (float(kel) * 9/5) - 459.67
    return round(fah, 2)
