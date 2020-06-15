numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers if num % 2 == 0]

print(doubled)

friends = ['John', 'Sam', 'Sylvia', 'Trelone']
starts_s = [friend for friend in friends if friend.startswith('S')]

print(starts_s)
