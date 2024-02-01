def bubble_sort(arr:list):
    swapmode = True
    while swapmode:
        swapmode = False
        for position in range(0,len(arr)-2):
            if arr[position] > arr[position+1]:
                arr[position], arr[position+1] = arr[position+1], arr[position]
                swapmode = True
            
    return arr

print(bubble_sort([1,4,6,3,2,6,8,7,3,6]))