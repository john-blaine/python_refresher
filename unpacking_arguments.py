def multiply(*args):
  total = 1
  for arg in args:
    total = total * arg
  return total

multiply(1, 3, 5)

#----------------------------

def add(x, y):
  return x + y

nums = [3, 5]

print(add(*nums))

#----------------------------

nums = { 'x': 15, 'y': 3 }

print(add(**nums))

#----------------------------

def apply(*args, operator):
  if operator == '*':
    return multiply(*args)
  elif operator == '+':
    return sum(args)
  else:
    return 'No valid operator provided to apply().'


print(f'This apply sum + (1, 2, 3) is {apply(1, 2, 3, operator="+")}')

print(f'This apply product * (1, 2, 3) is {apply(1, 2, 3, operator="*")}')
