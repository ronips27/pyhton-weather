# purwadhika

# stars sebagai wadah
stars = ''
size = 5

for i in range(size):
    for j in range(size - i):
        stars += '* '
    stars += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        stars += '* '
    stars += '\n'

print(stars)

for i in range(size):
    for j in range(size - i):
        stars += '  '
    for k in range(i * 2 + 1):
        stars += '* '
    stars += '\n'

for i in range(1, size):
    for j in range(i + 1):
        stars += '  '
    for k in range((size * 2) - (i * 2) -1):
        stars += '* '
    stars += '\n'

print(stars)