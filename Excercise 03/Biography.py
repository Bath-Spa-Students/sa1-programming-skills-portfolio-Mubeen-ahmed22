'''## Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.'''

# Step 1: Define the information as variables
Name = "Mubeen Ahmed"
Hometown = "pakistan"
Age = 17

user_info = {
    "Name": Name,
    "Hometown": Hometown,
    "Age": Age
}

# Step 2: Print the values on separate lines using a single print statement
print("Name:", user_info["Name"])
print("Hometown:", user_info["Hometown"])
print("Age:", user_info["Age"])


