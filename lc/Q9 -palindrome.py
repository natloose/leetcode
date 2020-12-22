# Check to see if a number is a Palindrome. Solve without string conversion


def isPalindrome(x):

    x = str(x)
    x = list(x)
    print(x)

    if len(x) <= 1:
        print("True")
    if len(x) > 1:
        while len(x) > 1:
            if x[0] == x[-1]:
                x.remove(x[0])
                x.remove(x[-1])
            else:
                break
    print("False")


isPalindrome(112202049204911)