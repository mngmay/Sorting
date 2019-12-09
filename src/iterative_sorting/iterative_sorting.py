# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr)-1):
            if(arr[i+1] < arr[i]):
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below

# Time: O(n+k), Space: O(n+k)
def count_sort(arr, maximum=-1):
    # count the number of occurences for each num in arr
    num_arr = [num for num in range(maximum+1)]
    count_arr = [0 for num in range(maximum+1)]

    for num in arr:
        count_arr[num] += 1

    print("step 1", "num_arr", num_arr, "count_arr", count_arr)
    # add each number to the right cumatively - index 0 stays the same
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    print("step 2", "num_arr", num_arr, "count_arr", count_arr)

    # starting index for each num = shift everything right 1 space, index 0 is 0
    count_arr[1:] = count_arr[0:-1]
    count_arr[0] = 0

    print("step 3", "num_arr", num_arr, "count_arr", count_arr)

    # initialize a new array the same length as the original array
    # iterate through the original array one by one
    # check the starting index from the array we constructed then increment by 1
    final_arr = [None] * len(arr)

    for num in arr:
        # index of num in num array
        target_index = num_arr.index(num)
        # count_arr[target_index] is the index in final_arr you want to insert the number
        final_arr[count_arr[target_index]] = num
        count_arr[target_index] += 1

    print("step 4", "num_arr", num_arr, "count_arr", count_arr)

    arr = final_arr

    return arr


print(count_sort([1, 0, 3, 1, 3, 1], 3))
