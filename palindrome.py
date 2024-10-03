def is_palindrome(num):
    original_num = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    return original_num == reverse_num

N = int(input(""))
M = int(input(""))

if 0 <= N <= 1000 and 0 <= M <= 1000:
    palindrome_count = 0

    for number in range(N, M + 1):
        if is_palindrome(number):
            palindrome_count += 1

    print(f'{palindrome_count}')
else:
    print(" N and M must be between 0 and 1000.")
