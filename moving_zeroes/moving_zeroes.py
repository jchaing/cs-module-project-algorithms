"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here

    # list to store all non zeros
    non_zeros = []

    # list to store all zeros
    zeros = []

    # loop through all index of list
    for i in range(len(arr)):

        # if element is 0, append to zeros list
        if arr[i] == 0:
            zeros.append(arr[i])

        # else, append non zero to non_zeros list
        else:
            non_zeros.append(arr[i])

    # combine non_zeros to zeros list
    return non_zeros + zeros


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
