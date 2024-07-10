# Function to calculate the sum of a list of numbers
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    # Ask the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of numbers
    numbers = list(map(int, user_input.split()))
    
    # Calculate the sum of the numbers
    total_sum = calculate_sum(numbers)
    
    # Display the result
    print(f"The sum of the numbers is: {total_sum}")

# Run the main function
if __name__ == "__main__":
    main()
