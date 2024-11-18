'''## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.'''

# Days of the Month

# Step 1: Making a Dictionary
days_of_months = {  
    1: 31,
    2: 28, 
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31 }

# Step 2: Input Management.
month = int(input("Enter month number (1-12): "))

# Step 3: Checking of the loops and the outputs.
if month in days_of_months:
    if month == 2:
        year = int(input("Is it a leap year? (Enter 1 for Yes, 0 for No): "))
        if year == 1:
            print("February has 29 days!!")
        else:
            print("February has 28 days!!")
    else:
        print(f"The month {month} has {days_of_months[month]} days.")
else:
    print("Month number was not able to match. Please enter a number between 1 and 12.")