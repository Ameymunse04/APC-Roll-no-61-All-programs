n = int(input("Enter a number: "))

i = 2
flag = 0

while i < n:
    if n % i == 0:
        flag = 1
        break
    i = i + 1

if n <= 1:
    print("Not a Prime Number")
elif flag == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")