'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    # store the product of all number in list
    prod_arr = []

    # make a copy of the list array
    copy_arr = arr.copy()

    for i in range(len(arr)):
        # set current indexed element to 1
        copy_arr[i] = 1

        # set initial product result to 1
        result = 1

        # loop through the and multiply each num from copied list
        for j in range(len(arr)):
            result = result * copy_arr[j]

        # append the product to the prod_arr list
        prod_arr.append(result)

        # make new copy of original array
        copy_arr = arr.copy()

    # return the list of all product of all other numbers
    return prod_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


arr = [1, 7, 3, 4]

print(product_of_all_other_numbers(arr))
