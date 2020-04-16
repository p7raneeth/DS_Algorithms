import math as m
def binsearch(values, key):
    n = len(values)-1
    l = 0
    h = n
    while(l<=h):
        mid = m.floor((l+h)/2)
        print(mid,l,h)
        if key == values[mid]:
            return mid
        elif key < values[mid]:
            h = mid-1
        else:
            l = mid + 1
    return 504
i = binsearch([1,2,3,4,5,6,], 1)
print(f'the index position of the key is {i}')