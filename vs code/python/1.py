# n = input()
# for char in n:
#     print(char)
# print(len(n))

# n = input()
# c=0
# for char in n:
#     c += 1
#     print(c)

# n = input()
# a = "aeiouAEIOU"
# c = 0
# for char in n:
#     if char in a:
#         c += 1
# print(c)

a = input()
rev = ""
for char in a:
    rev = char + rev
if a == rev:
    print("palindrome")
else:
    print("not palindrome")
    
