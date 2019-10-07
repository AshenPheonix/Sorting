# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i,len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index=x

        # TO-DO: swap
        temp=arr[i]
        arr[i]=arr[smallest_index]
        arr[smallest_index]=temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        swapped=False
        for x in range(0,len(arr)-i):
            if arr[x] > arr[x + 1]:
                swapped=True
                temp=arr[x]
                arr[x]=arr[x + 1]
                arr[x + 1] = temp
        
        if swapped==False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr