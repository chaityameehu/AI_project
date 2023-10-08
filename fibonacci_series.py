num1 = 0
num2 = 1
i = 10
print(num1)
print(num2)
for x in range (1,i):
    num3 = num1 + num2
    print(num3)
    num1, num2 = num2, num3
