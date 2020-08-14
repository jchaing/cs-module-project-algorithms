"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    # Your code here

    # list for single number
    single_list = []

    # loop through elements
    for i in arr:

        # check if current element is not in list, append it
        if i not in single_list:
            single_list.append(i)

        # if current element is in list, remove it
        else:
            single_list.remove(i)

    # return the single element number
    return single_list[0]


# arr = [1, 0, 1]
# print(single_number(arr))

if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

