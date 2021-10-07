import os
import requests

# check web server status
def status_code(url):
  r = requests.get(url)
  return r.status_code

# handle url inputs
def filter_url():
  for item in urls:  
    if (item.strip()[0:4]) != "http":
      item = "http://" + item
      filtered_urls.append(item.lower())
    else:
      filtered_urls.append(item.lower())

#print web server status if it is online or offline
def print_online_status():
  for i in filtered_urls:
    try:
      if status_code(i) == 200:
        print(f'{i} is up!')
      else:
        print(f'{i} is down!')
    except:
      print(f'{i[7:]} is not a valid URL.')

while True:
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check.(separated by comma)")
  urls = [item.strip(' ') for item in input().split(',')]
  filtered_urls = []
  
  filter_url()
  print_online_status()

  answer=None

  while True:
    answer = input('Do you want to start over? y/n ')
    if answer == 'y':
      break
    elif answer == 'n':
      print('k.bye!')
      break
      # exit()
    else:
      print(f'{answer} is not a valid answer')

  if answer == 'n':
    break