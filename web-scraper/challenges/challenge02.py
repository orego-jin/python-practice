#!/usr/bin/env python3


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def is_on_list(a, b):
  if b in a:
    return True
  else: 
    return False

def get_x(a,b):
  return a[int(b)]

def add_x(a,b):
  return a.append(b)

def remove_x(a,b):
  return a.remove(b)

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))
print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)