def hello():
  print('Hello')

hello()

def users_age_in_seconds():
  user_age = int(input('Enter your age: '))
  age_seconds = user_age * 365 * 24 * 60 * 60
  print(f'Your age in seconds is {age_seconds}')

print('Welcome to the age in seconds program')
users_age_in_seconds()
print('GoodBye!')

def add(x, y):
  result = x + y
  return result

print(f'The sum of 1 and 2 is {add(1, 2)}')

def say_hello(name, surname):
  print(f'Hello, {name} {surname}')

say_hello(surname='Blaine', name='John')
