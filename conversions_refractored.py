#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment6
"""

import conversions
import unittest

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, val):
    if fromUnit == "celsius" and toUnit == "kelvin":
        return conversions.CelsiusToKelvin(val)
    elif fromUnit == "celsius" and toUnit == "fahrenheit":
        return conversions.CelsiusToFahrenheit(val)
    elif fromUnit == "fahrenheit" and toUnit == "celsius":
        return conversions.FahrenheitToCelsius(val)
    elif fromUnit == "fahrenheit" and toUnit == "kelvin":
        return conversions.FahrenheitToKelvin(val)
    elif fromUnit == "kelvin" and toUnit == "fahrenheit":
        return conversions.KelvinToFahrenheit(val)
    elif fromUnit == "kelvin" and toUnit == "celsius":
        return conversions.KelvinToCelsius(val)

    
    elif fromUnit == "yards" and toUnit == "miles":
        miles = float(val) / 1760
        return round(miles, 2)
    elif fromUnit == "yards" and toUnit == "meters":
        meters = float(val) / 1.094
        return round(meters, 2)
    elif fromUnit == "meters" and toUnit == "yards":
        yards = float(val) * 1.094
        return round(yards, 2)
    elif fromUnit == "meters" and toUnit == "miles":
        miles = float(val) / 1609.344
        return round(miles, 2)
    elif fromUnit == "miles" and toUnit == "yards":
        yards = float(val) * 1760
        return round(yards, 2)
    elif fromUnit == "miles" and toUnit == "meters":
        meters = float(val) * 1609.344
        return round(meters,2)
    elif fromUnit == toUnit:
        return val

    else:
        raise ConversionNotPossible("Units are not compatible.")
