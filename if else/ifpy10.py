marital = input("Married or Unmarried (M/U): ")
gender = input("Gender (Male/Female): ")
age = int(input("Enter Age: "))

if marital == "M":
    print("Driver is Insured")
elif marital == "U":
    if gender == "Male" and age > 30:
        print("Driver is Insured")
    elif gender == "Female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")
else:
    print("Invalid Input")