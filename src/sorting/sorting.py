# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    merged_arr = []
    # Your code here
    arrA_index = 0
    arrB_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
    merged_arr += arrA[arrA_index:]
    merged_arr += arrB[arrB_index:]
    return merged_arr

    return merged_arr

def merge_sort(arr):
    """Merge sort algorithm implementation."""
    if len(arr) <= 1:  # base case
        return arr
    # divide array in half and merge sort recursively
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)

# # --------> Stack Overflow (start)<-------- # #
# # --> https://codereview.stackexchange.com/a/154136
# def merge(left, right):
#     """Merge sort merging function."""
#     left_index, right_index = 0, 0
#     result = []
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#     result += left[left_index:]
#     result += right[right_index:]
#     return result
# def merge_sort(array):
#     """Merge sort algorithm implementation."""
#     if len(array) <= 1:  # base case
#         return array
#     # divide array in half and merge sort recursively
#     half = len(array) // 2
#     left = merge_sort(array[:half])
#     right = merge_sort(array[half:])
#     return merge(left, right)
# # --------> Stack Overflow (finish)<-------- # #

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

