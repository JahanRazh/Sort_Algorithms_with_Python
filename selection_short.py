def selectionshort(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(1,n):
            if arr[min] > arr[j]:
                min = j

        arr[i],arr[min] = arr[min],arr[i]


arr =[12,6,7,8,10,2,12,9]
selectionshort(arr)
print(arr)

