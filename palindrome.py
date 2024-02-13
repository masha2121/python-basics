def is_palindrome(s):
    return s == s[::-1]


string = input("enter a string")
if is_palindrome(string):
    print("string is palindrome")
else:
    print("string not palindrome")

is_palindrome("string")
