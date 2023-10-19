# Program to convert celsius to Fahrenheit
def calc_fah(cel):
    fah = cel * 9/5 + 32
    return fah

celcius = float(input("Enter Celcius: "))
fahrenheit = calc_fah(celcius)

print(f"25 degrees is {fahrenheit} Fahrenheit")