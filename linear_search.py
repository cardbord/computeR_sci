def linear_search(arr:list,item:any):
    for i in range(len(arr)):
        if arr[i] == item:
            return i

print(linear_search([1,3,5,3,5,6,3,6,8,4,2,5,787,4,2],0))