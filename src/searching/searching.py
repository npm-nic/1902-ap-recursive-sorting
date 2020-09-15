# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # ---------> My thoughts here <---------
    # IF: check base case (sorted least to greatest)
        # IF: target is at mid
        # --> return the mid
        # ELIF: target is left of mid ( target < mid)
        # --> recursively run binary_search on range to left
        # --> [start...left_of_midpoint]
        # ELSE: target is right of mid (target > mid)
        # --> recursively run binary_search on range to right:
        # --> [right_of_midpoint ... end]
    # ELSE: not found
        # return -1
    # ---------> My code here <----------
    if end >= start:
        mid = (end + start) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)    
    else: # not found
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    return -1