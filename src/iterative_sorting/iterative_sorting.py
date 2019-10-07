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
    #test to check for array being non-empty
    if len(arr)<1:
        return []
    #get largest value if not given
    if maximum == -1:
        maximum=max(arr) + 1
    #make an array of all possible values
    temp=[0] * maximum
     
    #loop through array and increment that item by one. Throw error if negative number
    for item in arr:
        if item<0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            temp[item]+=1

    #return array
    ret=[]

    #loop over array and test 
    for i in range(0,len(temp)):
        ret += [i]*temp[i]

    arr=ret

    return arr