import requests

amount = int(input("How much would you like to convert? ")) 
from_currency = str(input("What currency would you like to convert from? " ))
to_currency = str(input("What currency would you like to convert to? " ))

def currency_converter(amount, from_currency, to_currency):
    # API endpoint
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    # Make request to API
    response = requests.get(url)
    data = response.json()
    # Get exchange rate for the given currency pair
    exchange_rate = data['rates'][to_currency]
    # Convert the amount to the target currency
    converted_amount = amount * exchange_rate
    return round(converted_amount, 2)

# Example usage:
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
