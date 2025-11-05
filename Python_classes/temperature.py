'''This file contains two functions
One for converting Celsius to Fahrenheit
and another for converting Fahrenheit to Celcius
However, we will add more measures in the feature'''


def to_fahrenheit(celsius):
    'This function converts Celsius to Fahrenheit'
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def to_celsius(fahrenheit):
    'This function converts Fahrenheit to Celsius'
    celsius = (fahrenheit - 32) * 5/9
    return celsius

outcome = to_fahrenheit(25)
print(outcome)