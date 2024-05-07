def merge_sort(arr, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid + 1, ub)
        merge(arr, lb, mid, ub)

def merge(arr, lb, mid, ub):
    n1 = mid - lb + 1
    n2 = ub - mid

    L = arr[lb:mid + 1]
    R = arr[mid + 1:ub + 1]

    i = j = 0
    k = lb

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [12, 6, 7, 8, 10, 2, 9]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
