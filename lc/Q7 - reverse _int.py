# 7. Reverse Integer


def reverse(x):
    if x >= 2 ** 31-1 or x < -2 ** 31: return 0
    else:
        # Stipulate the variable minus. If x is a negative number minus = -1 else = 1
        minus = -1 if x < 0 else 1
        x *= minus
        # Remove leading zeros in the reversed int
        while x:
            # while x mod 10 is equal to 0, divide it by 10
            while x % 10 == 0:
                x /= 10
            else:
                break
        # 1. String manipulation - Convert to String then List
        x = int(x)
        x = str(x)
        listed = list(x)
        # 2. Reverse List
        listed.reverse()
        # 3. Convert back to String sep=""
        rev = "".join(listed)
        # 4. Convert to Int
        x = int(rev)
        if x >= 2 ** 31 - 1 or x < -2 ** 31: return 0
        else:
            print(minus*x)

reverse(123)
