# pattern_drawing.py

# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row of the pattern
row = 0
while row < size:
    # Use a for loop to print asterisks side by side without a newline
    for col in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    row += 1
