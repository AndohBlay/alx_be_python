User = int(input("Enter the size of the pattern: "))

row = 0
while row < User:
    for col in range(User):
        print("*", end="")
    print()
    row += 1
