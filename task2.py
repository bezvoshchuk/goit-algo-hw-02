from collections import deque

def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    char_queue = deque(s)
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Example of usage
input_string = input("Введіть рядок для перевірки на паліндром: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")