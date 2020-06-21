def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError('Divisor cannot be 0.')

  return dividend / divisor

grades = []

print('Welcome to the average grade program.')
try:
  average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
  print(e)
  print('There are no grades yet.')
# As many except cases can be added as needed
# else runs only if the code in the try block executed
  # successfully
else:
  print(f'The average grade is {average}.')
finally:
  print('Thank you!')
