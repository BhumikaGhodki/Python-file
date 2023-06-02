#check string palindrome
def check(str):
    if str==str[::-1]:
        return "the string is a palindrome"
    else:
        return "The string is not a palindrome"
str=input("Enter string:")
print(check(str))