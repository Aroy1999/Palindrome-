def palindrome(name):
    if len(name)<=1:
        print("Palindrome")
    else:
        if name[0]==name[-1]:
            palindrome(name[1:-1])
        else:
            print("Not palindrome")

s=input()
palindrome(s)
