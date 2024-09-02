test = ['test1', 'test2', 'test3']
numbers = []

while True:
    var = len(numbers) + 1
    numbers.append(var)
    if len(numbers) == len(test):
        break

for number in numbers:
    print(number)