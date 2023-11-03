numbers = [42, 5, 1, 3, 89, 32]

minVal = numbers[0]
maxVal = numbers[0]

for num in numbers:
    if(num < minVal):
        minVal = num
    if(num > maxVal):
        maxVal = num 

print("Numbers = {}".format(numbers))
print("Minimum Value = {}".format(minVal))
print("Maximal VAlue = {}".format(maxVal))
