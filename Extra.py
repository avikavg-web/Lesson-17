number = int(input("Give me a number"))

for i in range(1, number, 1):
    if i%10 == 0:
        print(i)
        continue