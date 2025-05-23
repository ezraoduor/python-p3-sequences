#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length <= 0:
        print([])
        return
    
    # Initialize the Fibonacci sequence list
    fib_list = [0]  # Start with the first Fibonacci number
    
    # If length is 1, print just [0]
    if length == 1:
        print(fib_list)
        return
    
    # Add the second Fibonacci number
    fib_list.append(1)
    
    # Generate subsequent Fibonacci numbers
    for i in range(2, length):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    # Print the resulting list
    print(fib_list)
    pass