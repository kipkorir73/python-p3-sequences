def print_fibonacci(length):
    fib_sequence = [0, 1]

    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    formatted_sequence = ', '.join(map(str, fib_sequence))
    print(f"[{formatted_sequence}]")


print_fibonacci(9)
