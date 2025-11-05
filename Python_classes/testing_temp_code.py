import temperature as t

for i in range (-40, 100, 20):
    result = t.to_celsius(i)
    print(f"{i} Fahrenheit is: {result:.2f} Celsius")