import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

url="https://www.iban.com/currency-codes"
request=requests.get(url)
soup=BeautifulSoup(request.text, "html.parser")

table=soup.find("table")
rows=table.find_all("tr")[1:]
# print(rows[:10])
countries=[]

for i in rows:
  items = i.find_all("td")
  name= items[0].text
  code= items[2].text

  if name and code:
    country={
      'name': name.capitalize(),
      'code': code
    }
  countries.append(country)
  
def print_result(choice):
  user_country = countries[choice]
  selected_countries.append(user_country)
  print(f"\n{user_country['name']}")
  
selected_countries =[]

def main():
  try:
    first_choice = int(input("\n#: "))
    if first_choice in range(len(countries)):
      print_result(first_choice)
      print("\nNow choose another country.\n")

      def second_country():
        second_choice = int(input("#:"))
        if second_choice in range(len(countries)):
          print_result(second_choice)
          print(f"\nHow much {selected_countries[0]['code']} do you want to convert to {selected_countries[1]['code']}?")
    
          def currency_calculator():
            amount= int(input())
            c_from=selected_countries[0]['code'].lower()
            c_to=selected_countries[1]['code'].lower()
            currency_url=f"https://wise.com/gb/currency-converter/{c_from}-to-{c_to}-rate"
            try:
              currency_request=requests.get(currency_url)
              currency_soup=BeautifulSoup(currency_request.text, "html.parser")
              exchange_rate=currency_soup.find("span", {"class": "text-success"}).text
              original_amount=format_currency(amount, c_from.upper())
              converted_amount=format_currency(float(amount)*float(exchange_rate), c_to.upper(), locale='en_US')
              print(f"{original_amount} is {converted_amount}")
            except:
              print("Currency exchange rate not found.")

          try:
           currency_calculator()
          except:
            print("That wasn't a number")

        else:
          print("Choose a number from the list")
          second_country()

      try:
        second_country()
      except:
        print("That wasn't a number")
        second_country()

    else:
      print("Choose a number from the list")
      main()

  except:
    print("That wasn't a number")
    main()

#program starts here
print('Welcome to CurrencyConvert PRO 2000\n')
for (index, item) in enumerate(countries):
  print(f"#{index} {item['name']}") 
print('\nWhere are you from? Choose a country by number.')
main()
