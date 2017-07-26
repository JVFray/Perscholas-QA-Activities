def temp():
    celsius  = int(input("Give me a temperature in Fahrenheit"))
    fahrenheit = (celsius - 30) * 2
    print("Your Celsius temperature is", celsius)
    print("Your Fahrenheit temperature is", fahrenheit)


temp()
i = input("Do you want to still use this program?")
while i != 'no':
    temp()

print("Have a great day!!")