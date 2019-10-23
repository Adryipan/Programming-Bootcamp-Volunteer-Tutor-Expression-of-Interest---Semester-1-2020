#Read a list of integers from user input.
numbers = list()
totalNumber = 0
next = False
while not next:
    try:
        totalNumber = int(input('How many numbers are you putting in?'))
        if totalNumber > 1:
            next = True
        else:
            print("There are no pair.... Input a number that is larger than 1.....")
    except:
        print('Please input a number.')

print('Start:')
i = 0
while i < totalNumber:
    try:
        userInput = int(input())
        numbers.append(userInput)
        i += 1
    except:
        print('Please input a number')


#Find all pairs of numbers in the list whose
productEven = list()
sumOdd = list()
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if ((numbers[i] * numbers[j]) % 2) == 0: # product is even
            productEven.append((numbers[i], numbers[j]))

        if ((numbers[i] + numbers[j]) % 2) != 0: # sum is odd
            sumOdd.append((numbers[i], numbers[j]))

#Print out a formatted list of the pairs.
print()
print('Pair of numbers with even product:')
i = 1
for thisPair in productEven:
    print('Pair {2}: {0}, {1}'.format(thisPair[0], thisPair[1], i))
    i += 1

print()
print('Pair of numbers with odd sum:')
i = 1
for thisPair in sumOdd:
    print('Pair {2}: {0}, {1}'.format(thisPair[0], thisPair[1], i))
    i += 1

