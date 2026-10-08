n = int(input("Enter how many numbers: "))

count = 1

num = int(input("Enter number: "))
smallest = num

while count < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    count = count + 1

print("Smallest number =", smallest)