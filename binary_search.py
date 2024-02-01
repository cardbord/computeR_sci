def binary_search(arr:list,item):
    arr.sort()
    uprange = len(arr)-1
    downrange = 0
    while 1: 
        midp = (uprange+downrange)//2
        if item == arr[midp]:
            return midp
        elif item > arr[midp]:
            downrange = midp
        elif item < arr[midp]:
            uprange = midp
        else:
            break
    return midp

print(binary_search([1,2,3,4,5,6,7,8,9],7))