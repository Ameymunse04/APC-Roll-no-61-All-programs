n = int(input("Enter how many numbers: "))

count = 1

num = int(input("Enter number: "))
largest = num

while count < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    count = count + 1

print("Largest number =", largest)