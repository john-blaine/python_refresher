print((lambda x, y: x + y)(5, 7))

def double(x):
  return x * 2

sequence = [1, 2, 3, 5, 8]
# The below in comments on both lines is doing the same thing as the line below it
# doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
