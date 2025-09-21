num = int(input('Enter the number: '))
fact = 1

for i in range(1, num + 1):
    fact *= i

print('Factorial of', num, 'is:', fact)


#using while loop
num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print('Factorial is', fact)