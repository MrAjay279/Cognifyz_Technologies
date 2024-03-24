def generate_fibonacci_sequence(terms):
    fibo_seq = []

    # Check if the number of terms is valid
    if terms <= 0:
        return fibo_seq

    fibo_seq.append(0)
    if terms > 1:
        fibo_seq.append(1)

    for i in range(2, terms):
        next_term = fibo_seq[i - 1] + fibo_seq[i - 2]
        fibo_seq.append(next_term)

    return fibo_seq


# Main Code
num_terms = int(input("Enter the number of terms : "))

# Generate and display the Fibonacci sequence
fib_sequence = generate_fibonacci_sequence(num_terms)

print("Fibonacci sequence up to", num_terms, "terms:",end=" ")

for num in fib_sequence:
    print(num, end = " ")
