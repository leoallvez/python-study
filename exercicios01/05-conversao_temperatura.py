def celsius_to_fahenheit(c):
    return c * (9.0 / 5.0) + 32.0


def fahenheit_to_celsius(f):
    return 5.0 * (f - 32.0) / 9.0


def kelvin_to_celsius(k):
    return k - 273.15


def celsius_to_kelvin(c):
    return c + 273.15


# celsius = float(input("digite a temperatura em celsius: "))
# print(f"Temperatura em Fahrenheit: {celsius_to_fahenheit(celsius)}")

# fahenheit = float(input("digite a temperatura em fahenheit: "))
# print(f"Temperatura em Celsius: {fahenheit_to_celsius(fahenheit)}")

# kelvin = float(input("digite a temperatura em kelvin: "))
# print(f"Temperatura em Celsius: {kelvin_to_celsius(kelvin)}")

celsius = float(input("digite a temperatura em celcius: "))
print(f"Temperatura em Kelvin: {celsius_to_kelvin(celsius)}")
