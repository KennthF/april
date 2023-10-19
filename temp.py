# Program to convert celsius to Fahrenheit
def cal_fah(cel):
    fah = cel * 9/5 + 32
    return fah
    
user = float(input("Enter Celcius: "))

fahrenheit = cal_fah(user)

print(f"25 degrees is {fahrenheit} Fahrenheit")