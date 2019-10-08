# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0]>arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))

    if len(arrA) > 0:
        merged_arr+=arrA
    else:
        merged_arr+=arrB
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(arr)
    if len(arr) > 1:
        low = merge_sort(arr[:len(arr)//2])
        high = merge_sort(arr[len(arr)//2:])
        arr=merge(low,high)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    if start == mid or mid == end or start == end:
        return arr
    else:
        while start<mid and end>mid:
            if arr[start]>arr[mid]:
                for i in range(start,mid+1):
                    temp=arr[start]
                    arr[start]=arr[i]
                    arr[i]=temp
                mid+=1
            start+=1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if isinstance(arr, list)!=False:
        return
    if r-l>2:
        merge_sort_in_place(arr,l,( l + ( (r-l)//2) ))
        merge_sort_in_place(arr,( l + ( (r-l)//2) )+1,r)
    merge_in_place(arr,l,l + ((r-l)//2),r )
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
