n = int(input("Enter the number of rows: "))

for i in range(n,0,-1):
    for j in range(i):
        print(chr(97 + j), end="")
    print()