


def plus(a,b):
  return a+b

def minus(a,b):
  return a-b

def muliply(a,b):
  return a*b

def divide(a,b):
  return a/b

def remainder(a,b):
  return a%b

def power(a,b):
  return pow(a,b)

def negation(a):
  return -a


def age_check(age):
  print(f"you are {age} years old")
  if age < 18:
    print("you are too young")
  elif age == 18 or age ==19:
    print("you are new!")
  elif age >20 and age < 25:
    print("you are kind of young")
  else:
    print("enjoy your drink")

age_check(21)

