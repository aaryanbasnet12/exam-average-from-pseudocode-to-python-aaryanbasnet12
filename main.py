"""
Pseudocode:

1. Ask the user to enter the first exam score.
2. Ask the user to enter the second exam score.
3. Ask the user to enter the third exam score.
4. Convert all three inputs into integers.
5. Define a function named compute_average that:
       - Takes three exam scores as parameters.
       - Adds the three scores together.
       - Divides the total by 3 to get the average.
       - Returns the average.
6. Call the compute_average function using the three scores entered by the user.
7. Store the returned average in a variable.
8. Print the first score on its own line.
9. Print the second score on its own line.
10. Print the third score on its own line.
11. Print the final average on its own line.
"""



# Ask the user for the first score
first_score = int(input("Enter first score: "))

# Ask the user for the second score
second_score = int(input("Enter second score: "))

# Ask the user for the third score
third_score = int(input("Enter third score: "))

# Define a function to compute the average of three scores
def compute_average(a, b, c):
    # Return the average of the three values
    return (a + b + c) / 3

# Call the function and save the result in average_score
average_score = compute_average(first_score, second_score, third_score)

# Print the first score
print("First score:", first_score)

# Print the second score
print("Second score:", second_score)

# Print the third score
print("Third score:", third_score)

# Print the average score
print("The average score is:", average_score)
