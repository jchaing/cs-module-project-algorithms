"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Your code here

    j = k + 1

    cur_max = max(nums[:k])

    max_list = [cur_max]

    for i in range(1, len(nums)):
        if j <= len(nums):
            cur_max = max(nums[i:j])
            max_list.append(cur_max)
            j += 1
        else:
            break

    return max_list

    # # runs in about 5 seconds
    # cur_max = max(nums[:k])
    # max_list = [cur_max]
    # for i in range(k, len(nums)):
    #     if nums[i] > cur_max:
    #         cur_max = nums[i]
    #     elif cur_max == nums[i - k]:
    #         cur_max = max(nums[(i - k + 1):(i + 1)])
    #     max_list.append(cur_max)
    # return max_list

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
