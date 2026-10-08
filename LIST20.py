# # 1. Write a Python program to create a list of five fruits and display the list.
# l = ["APPLE", "BANANA", "MANGO", "GRAPES"]
# print(l)


# # 2. Create a list of five integers. Display:
# # •	First element
# # •	Last element
# # •	Third element

# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Third element:", numbers[2])



# # 3.	Create a list of colors. Replace the third color with another color and display the updated list.
# colors = ["Red", "Blue", "Green", "Yellow"]

# colors[2] = "Pink"

# print(colors)



# # 4.	Create a list of numbers. Add:
# # •	One element at the end
# # •	One element at the beginning
# # •	One element at a specified position Display the updated list.

# nums = [10, 20, 30, 40]

# nums.append(50)       # Add at end
# nums.insert(0, 5)     # Add at beginning
# nums.insert(2, 15)    # Add at position 2

# print(nums)



# # 5. Create a list of student names. Remove:
# # •	First student
# # •	Last student
# # •	A specific student by name
# # Display the remaining list.

# students = ["Rahul", "Amit", "Sneha", "Priya", "Rohan"]

# students.pop(0)          # Remove first
# students.pop()           # Remove last
# students.remove("Sneha") # Remove specific student

# print(students)



# # 6.	Write a program to find the largest and smallest number in a list without using max() or min().
# n = [45, 12, 78, 23, 9, 56]

# largest = n[0]
# smallest = n[0]

# for num in n:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)



# # 7.	Accept 10 numbers from the user and store them in a list. Calculate:
# # •	Sum
# # •	Average
# li = []

# for i in range(10):
#     num = int(input("Enter number: "))
#     li.append(num)

# total = 0

# for num in li:
#     total = total + num

# average = total / 10

# print("Sum:", total)
# print("Average:", average)



# 8. Store 15 integers in a list. Count how many numbers are:
# •	Even
# •	Odd
# numbers = []

# for i in range(15):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# even = 0
# odd = 0

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even numbers:", even)
# print("Odd numbers:", odd)



# 9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
# cities = ["Mumbai", "Pune", "Delhi", "Kolkata", "Chennai"]

# city = input("Enter city name: ")

# if city in cities:
#     print("City exists in the list")
# else:
#     print("City does not exist")



#. 10.	Write a program to reverse a list without using the reverse() method.
# numbers = [10, 20, 30, 40, 50]

# reversed_list = []

# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])

# print("Original list:", numbers)
# print("Reversed list:", reversed_list)



# 11. Create a list of 10 numbers and display:
#  First 5 elements
#  Last 5 elements
#  Middle 4 elements
#  Alternate elements
#  Reverse list using slicing

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print("First 5 elements:", numbers[:5])

# print("Last 5 elements:", numbers[-5:])

# print("Middle 4 elements:", numbers[3:7])

# print("Alternate elements:", numbers[::2])

# print("Reverse list:", numbers[::-1])



# 12. Display all elements present at even index positions
# numbers = [10, 20, 30, 40, 50, 60, 70]

# for i in range(len(numbers)):
#     if i % 2 == 0:
#         print(numbers[i])



# 13. Accept 10 numbers and sort them in:
#  Ascending order
#  Descending order
# numbers = []

# for i in range(10):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# numbers.sort()

# print("Ascending order:", numbers)

# numbers.sort(reverse=True)

# print("Descending order:", numbers)



# 14. Create a list containing duplicate values and display only unique elements
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print("Unique elements:", unique)



# 15. Find the second largest element in a list.
# numbers = [10, 50, 30, 80, 40, 70]

# numbers.sort()

# print("Second largest:", numbers[-2])



#16.Create a nested list storing:
#  Student Name
#  Roll Number
#  Marks

# students = [
#     ["Rahul", 101, 85],
#     ["Amit", 102, 90],
#     ["Sneha", 103, 78]
# ]

# for student in students:
#     print("Name:", student[0])
#     print("Roll Number:", student[1])
#     print("Marks:", student[2])
#     print()



#17.Create two 3 × 3 matrices using nested lists and performmatrix addition.

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# result = []

# for i in range(3):
#     row = []

#     for j in range(3):
#         row.append(matrix1[i][j] + matrix2[i][j])

#     result.append(row)

# print("Matrix Addition:")

# for row in result:
#     print(row)


#18.Create a shopping cart using a list.
# Perform:
#  Add item
#  Remove item
#  Search item
#  Display cart
#  Count total items

# cart = []

# cart.append("Laptop")
# cart.append("Mouse")
# cart.append("Keyboard")

# print("Cart:", cart)

# cart.remove("Mouse")

# print("After removing Mouse:", cart)

# item = input("Enter item to search: ")

# if item in cart:
#     print("Item is available")
# else:
#     print("Item is not available")

# print("Shopping Cart:", cart)

# print("Total items:", len(cart))



#19.Store names of students present in class.
# Display:
#  Total students
#  Search a student's attendance
#  Add a new student
#  Remove an absent student

# students = ["Rahul", "Amit", "Sneha", "Priya"]

# print("Total students:", len(students))

# name = input("Enter student name to search: ")

# if name in students:
#     print("Student is present")
# else:
#     print("Student is absent")

# new_student = input("Enter new student name: ")
# students.append(new_student)

# absent = input("Enter absent student name: ")

# if absent in students:
#     students.remove(absent)

# print("Final student list:", students)



#20.Create a list of books.
# Implement:
#  Add a new book
#  Search a book
#  Remove a book
#  Display all books
#  Count total books

books = ["Python", "Java", "C++", "HTML"]

new_book = input("Enter new book: ")
books.append(new_book)

search = input("Enter book to search: ")

if search in books:
    print("Book found")
else:
    print("Book not found")

remove = input("Enter book to remove: ")

if remove in books:
    books.remove(remove)

print("Books:", books)

print("Total books:", len(books))