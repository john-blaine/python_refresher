family = {'John': 31, 'Naomi': 33, 'Auria': 5}

for member, age in family.items():
  print(f'{member} is {age} years old')

coworkers = [( 'Eric', 32, 'Tech Lead' ), ( 'Tim', 38, 'Tech Lead' ), ( 'Ryan', 27, 'Front-end Dev' )]

for name, age, profession in coworkers:
  print(f'Name: {name}, Age: {age}, Profession: {profession}')
