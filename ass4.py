n = int(input("Enter the value of n: "))
print(f"Odd numbers up to {n} are:")
for i in range(1, n + 1):
    if i % 2 != False:
        print(i, end=" ")
