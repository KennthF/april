# Program to convert celsius to Fahrenheit
def calc_fahrenheit(cel):
    fah = cel * 9/5 + 32
    return fah

def calc_celcius(fah):
    cel = 5/9 * (fah - 32)
    return cel




user = float(input("Enter a Celcius: "))

fahrenheit = calc_fahrenheit(user)
celcius = calc_celcius(fahrenheit)

print(f"The {user} degrees celcius is {fahrenheit} Fahrenheit")
print(f"The {fahrenheit} degrees fahrenheit is {celcius} celcius")