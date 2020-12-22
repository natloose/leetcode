# Q1. Two Sum

array = [2,7,11,15]
targ = 9


def twoSum(arr, target):
    # Create empty dictionary
    values = {}
    # Loop through arr for indices and values
    for i, num in enumerate(arr):
        # Create difference variable for later comparison
        diff = target - num
        # Check to see if diff is in values, if so return idces of both nums
        if diff in values:
            return values[diff], i
        # Add value to dictionary
        values[num] = i
    return


twoSum(arr=array, target=targ)

