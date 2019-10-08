#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment6
"""

import conversions_refractored
import unittest

class KnownValues(unittest.TestCase):
    #known values to test temperature conversion
    
    known_values_temp = (('celsius', 'kelvin', 50.00, 323.15),
                    ('celsius', 'fahrenheit', 50.00, 122.00),
                    ('fahrenheit', 'kelvin', 122.00, 323.15),
                    ('fahrenheit', 'celsius', 122.00, 50.00),
                    ('kelvin', 'fahrenheit', 323.15, 122.00),
                    ('kelvin', 'celsius', 323.15, 50.00))
                    
    print("*****Testing temperature conversion*****")
    def testTempConversion(self):
        #Test to see if temperature conversions are correct
        for fromUnit, toUnit, val, result in self.known_values_temp:
            output = conversions_refractored.convert(fromUnit, toUnit, val)
            self.assertEqual(result, output)

    known_values_distance = (('yards', 'miles', 1000.00, 0.57),
                    ('yards', 'meters', 1000.00, 914.08),
                    ('meters', 'yards', 914.08, 1000.00),
                    ('meters', 'miles', 402.34, 0.25),
                    ('miles', 'yards', 0.57, 1003.20),
                    ('miles', 'meters', 0.25, 402.34))
                    
    print("*****Testing distance conversion*****")
    def testDistanceConversion(self):
        #Test to see if distance conversions are correct
        for fromUnit, toUnit, val, result in self.known_values_distance:
            output = conversions_refractored.convert(fromUnit, toUnit, val)
            self.assertEqual(result, output)

    known_values_convertingtoself = (('yards', 'yards', 100, 100),
                    ('meters', 'meters', 50, 50),
                    ('celsius', 'celsius', 10, 10),
                    ('kelvin', 'kelvin', 500, 500))

    print("*****Testing conversion of one unit to itself*****")
    def testSelfConversion(self):
        #Test to see if converting to self returns input valie
        for fromUnit, toUnit, val, result in self.known_values_convertingtoself:
            output = conversions_refractored.convert(fromUnit, toUnit, val)
            self.assertEqual(result, output)


    print("*****Testing conversion of incompatible units will raise ConversionNotPossible exception*****")
    def testConversionException(self):
        #Test to see if converting incompatible units raise exception
        self.assertRaises(conversions_refractored.ConversionNotPossible, conversions_refractored.convert, "yards", "fahrenheit", 10)

if __name__ == '__main__':
    unittest.main()
            
