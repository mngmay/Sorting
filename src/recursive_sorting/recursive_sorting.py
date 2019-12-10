# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    print("initial", arrA, arrB)

    # keep track of index for arrA
    i = 0
    # keep track of index for arrB
    j = 0
    # keep track of index for merged_array
    k = 0

    # while both arrays have values
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            # add smallest value to merged_arr
            merged_arr[k] = arrA[i]
            # increment to view next index of arrA and merged_arr
            i += 1
            k += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
            k += 1

    # take care of conditions when a subarray is empty, apply the same logic to the remaining array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    print(merged_arr)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    # split array in half
    midpoint = int(len(arr)/2)

    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
