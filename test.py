#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment6
"""

import conversions
import unittest

class KnownValues(unittest.TestCase):
    #known values to test temperature conversion Celcius, Farenheit, and Kelvin
    known_values = ((-100.00, -148.00, 173.15),
                    (-50.00, -58.00, 223.15),
                    (0.00, 32.00, 273.15),
                    (50.00, 122.00, 323.15),
                    (100.00, 212.00, 373.15),
                    (150.00, 302.00, 423.15),
                    (200.00, 392.00, 473.15))

    def testCelsiusToFahrenheit(self):
        #Test to see if CelsiusToFarenheit returns the second number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.CelsiusToFahrenheit(cel)
            self.assertEqual(fah, result)

    def testCelsiusToKelvin(self):
        #Test to see if CelsiusToKelvin returns the third number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.CelsiusToKelvin(cel)
            self.assertEqual(kel, result)

    def testFahrenheitToCelsius(self):
        #Test to see if FarenheitToCelsius returns the first number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.FahrenheitToCelsius(fah)
            self.assertEqual(cel, result)

    def testFahrenheitToKelvin(self):
        #Test to see if FarenheitToKelvin returns the third number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.FahrenheitToKelvin(fah)
            self.assertEqual(kel, result)

    def testKelvinToCelsius(self):
        #Test to see if KelvinToCelsius returns the first number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.KelvinToCelsius(kel)
            self.assertEqual(cel, result)

    def testKelvinToFahrenheit(self):
        #Test to see if KelvinToFarenheit returns the first number in known values
        for cel, fah, kel in self.known_values:
            result = conversions.KelvinToFahrenheit(kel)
            self.assertEqual(fah, result)

if __name__ == '__main__':
    unittest.main()
            
