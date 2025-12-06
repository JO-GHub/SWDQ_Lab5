# Unit test for WeatherData.py
# Included some other Unit Test methods

import unittest

# importing WeatherData class from WeatherData module
from WeatherData import WeatherData

# create test case that inherits from 'unittest.TestCase'
class TestWeatherData(unittest.TestCase):
    def test1_collect_data(self):
        print('test1\ncollect data')
        
        # create weather station
        station_1 = WeatherData()
        
        # test lists are empty initially
        self.assertTrue(len(station_1.airTemp) == 0)
        
        # collect weather data
        station_1.collectWeatherData(18, 22, "N")
        
        # test data was stored
        self.assertEqual(len(station_1.airTemp), 1)
        self.assertEqual(station_1.airTemp[0], 18)
        self.assertEqual(station_1.windSpeeds[0], 22)
        self.assertEqual(station_1.windDirections[0], "N")
        
        # test lists are not empty
        self.assertFalse(len(station_1.airTemp) == 0)

        station_1.summarise()

    def test2_multiple_readings(self):
        print('test2\nmultiple readings')
        
        # create weather station
        station_1 = WeatherData()
        
        # collect multiple readings
        station_1.collectWeatherData(18, 22, "N")
        station_1.collectWeatherData(9, 28, "SW")
        
        # test multiple readings stored
        self.assertEqual(len(station_1.airTemp), 2)
        
        self.assertEqual(station_1.airTemp[0], 18)
        self.assertEqual(station_1.windSpeeds[0], 22)
        self.assertEqual(station_1.windDirections[0], "N")
        
        self.assertEqual(station_1.airTemp[1], 9)
        self.assertEqual(station_1.windSpeeds[1], 28)
        self.assertEqual(station_1.windDirections[1], "SW")
        
        # test direction is in list
        self.assertIn("N", station_1.windDirections)
        self.assertIn("SW", station_1.windDirections)

        station_1.summarise()
        
    def test3_average_calculation(self):
        print('test3\naverage calculation')
        
        station_1 = WeatherData()
        station_1.collectWeatherData(18, 22, "N")
        station_1.collectWeatherData(9, 28, "SW")
        
        # calculate expected average
        expected_avg = (18 + 9) / 2
        actual_avg = sum(station_1.airTemp) / len(station_1.airTemp)
        
        # test average calculation
        self.assertEqual(expected_avg, actual_avg)
        
        # test value is correct type
        self.assertIsInstance(actual_avg, float)
        
        # print only average
        print(f"Average Temp in °C = {actual_avg:.1f} °C")
        
if __name__ == '__main__':
    unittest.main()