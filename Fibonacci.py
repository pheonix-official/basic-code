def generate_fibonacci(n):
    # Initialize an empty list to store the Fibonacci sequence.
    fibonacci_sequence = []

    # Initialize two variables to keep track of the current and next Fibonacci numbers.
    a, b = 0, 1

    # Loop to generate the first n Fibonacci numbers.
    for _ in range(n):
        # Append the current Fibonacci number (a) to the sequence.
        fibonacci_sequence.append(a)

        # Calculate the next Fibonacci number by adding a and b, then update a and b.
        a, b = b, a + b

    # Return the list of Fibonacci numbers.
    return fibonacci_sequence


if __name__ == "__main__":
    # Prompt the user for input to specify the number of Fibonacci numbers to generate.
    n = int(input("Enter the number of Fibonacci numbers to generate: "))

    # Check if the user provided a non-positive integer.
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Call the generate_fibonacci function to generate the Fibonacci sequence.
        fibonacci_numbers = generate_fibonacci(n)

        # Print the resulting list of Fibonacci numbers.
        print(f"The first {n} Fibonacci numbers are:")
        print(fibonacci_numbers)
