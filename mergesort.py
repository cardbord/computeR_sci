#garbarj
import timeit
import random as r

#arr = [r.randrange(1,100) for _ in range()]


def mergesort(data:list):
    if len(data)>1:
        lhalf = data[:len(data)//2]
        rhalf = data[len(data)//2:]
        mergesort(rhalf)
        mergesort(lhalf)
        
        i=0
        j=0
        k=0
        
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[i]:
                data[k]=lhalf[i]
                i+=1
            else:
                data[k]=rhalf[j]
                j+=1
            k+=1
        while i < len(lhalf):
            data[k]=lhalf[i]
            i+=1
            k+=1
        while j < len(rhalf):
            data[k] = rhalf[j]
            j+=1
            k+=1
    return data

alist = [5,3,6,8,4,3,4,5,6]

print(alist, len(alist))
alist = mergesort(alist)
print(alist)