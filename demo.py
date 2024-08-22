
def print_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (2 * (n - i)) + ' ' * (2 * i - 1) + ' ' * (2 * (n - i)) + '*' * (2 * i - 1))

    for i in range(n , 2 * n):
        print(' ' * (i+(n-1)) + '*' * (2 * (2 * n - i) - 1))


n = int(input("Enter the height of the pattern: "))
print_pattern(n)
