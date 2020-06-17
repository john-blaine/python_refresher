def multiply(*args):
  print(args)
  total = 1
  for arg in args:
    total = total * arg
  print(total)

multiply(1, 3, 5)

#----------------------------

def add(x, y):
  return x + y

nums = [3, 5]

print(add(*nums))

#----------------------------

nums = { 'x': 15, 'y': 3 }

print(add(**nums))
