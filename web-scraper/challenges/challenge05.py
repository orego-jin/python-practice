import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def extract_country_info():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  country_name = soup.select("td:first-child")
  currency_code=soup.select("td:nth-child(3)")
  countries=[]
  currency_codes=[]

  for i in country_name:
    countries.append(i.text)

  for i in currency_code:
    currency_codes.append(i.text)
  
  zip_iterator = zip(countries, currency_codes)
  currency_dict = dict(zip_iterator)

  for (i, item) in enumerate(countries):
    print(i, item)
  

  # print(currency_dict)
  def user_input():
    try:
      selected_country_index = int(input(""))

      if selected_country_index in range(len(countries)):
        selected_country_name = countries[selected_country_index]
        print("The currency code is", currency_dict[selected_country_name])

      else:
        print("Choose a number from the list")
        user_input()
    except:
      print("That wasn't a number")
      user_input()

  user_input()

print("Hello please select a country by number:")
extract_country_info()
