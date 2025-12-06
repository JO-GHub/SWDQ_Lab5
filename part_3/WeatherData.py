# https://www.w3schools.com/python/python_classes.asp
# https://www.w3schools.com/python/python_class_init.asp
# https://www.w3schools.com/python/python_class_self.asp
# https://www.w3schools.com/python/python_class_properties.asp
# https://www.w3schools.com/python/python_class_methods.asp
# https://www.w3schools.com/python/python_arrays.asp
# https://www.w3schools.com/python/python_strings.asp
# https://www.w3schools.com/python/python_operators_arithmetic.asp
# https://www.w3schools.com/python/python_string_formatting.asp
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V

# Thank you to a previously unfinished CS50P playlist and W3Schools

class WeatherData:
    # declare attributes
    def __init__(self):
        self.airTemp = []
        self.windSpeeds = []
        self.windDirections = []
    
    # store collected weather data
    def collectWeatherData(self, temp, speed, direction):
        self.airTemp.append(temp)
        self.windSpeeds.append(speed)
        self.windDirections.append(direction)
    
    # i presume this is formatting weather data and presenting it
    def summarise(self):
        # format as float to 1 decimal point
        # [-1] to indicate last variable in array
        print(f"Current Temp in °C=  {self.airTemp[-1]:.1f} °C")
        print(f"Current Wind Speed in Km/h=  {self.windSpeeds[-1]:.1f} Km/h")
        print(f"Current Cardinal Wind Direction = {self.windDirections[-1]}")

        # average temperature reading
        avg_temp = sum(self.airTemp) / len(self.airTemp)
        print(f"Average Temp °C=  {avg_temp:.1f} °C\n")

# uncomment when running WeatherData.py as a standalone
# comment out when using the Unit Test so it doesnt echo
"""
def main():
        station_1 = WeatherData()
        station_1.collectWeatherData(18, 22, "N")
        station_1.collectWeatherData(9, 28, "SW")
        station_1.summarise()

main()
"""