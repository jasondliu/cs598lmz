import threading
threading.stack_size(67108864)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(digits):
    first = 10 ** (digits - 1)
    last = 10 ** digits - 1
    largest = 0
    for i in range(first, last + 1):
        for j in range(first, last + 1):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest

def largest_palindrome_product_threaded(digits):
    first = 10 ** (digits - 1)
    last = 10 ** digits - 1
    largest = 0
    results = []
    # Create a thread for each iteration of the outer loop
    threads = [threading.Thread(target=lambda: results.append(largest_palindrome_product(digits))) for i in range(first, last + 1)]
    for thread in threads:
        thread.start()
    for thread in threads
