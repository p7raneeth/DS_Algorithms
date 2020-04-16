# complete Binary Tree --> Max Heap
#list = [50,30,40,10,20,8,27]

# Insert operation into a Heap Tree
import math as m
def insertElem(list, elem):
    list.append(elem)
    import math as m
    length = len(list)
    idx = list.index(list[-1])
    idx_elem = list.index(elem)
    for i in range(int(m.log(length,2))):
        if idx%2 != 0:
            if list[m.floor(idx/2)] < elem:
                list[m.floor(idx/2)], list[idx_elem] = list[idx_elem], list[m.floor(idx/2)]
                idx = m.floor(idx/2)
                print(idx)
                idx_elem = list.index(elem)
            else:
                return list
        else:
            print('even')
            if list[m.floor(idx/2)-1] < elem:
                list[m.floor(idx/2)-1], list[idx_elem] = list[idx_elem], list[m.floor(idx/2)-1]
                idx = m.floor(idx/2)-1
                idx_elem = list.index(elem)
            else:
                return list
    return list

print(insertElem([50,30,40,10,20,8,27,1,2,15], 60))
