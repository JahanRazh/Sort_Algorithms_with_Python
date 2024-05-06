def partition(array, lb, ub):
    pivot = array[lb]
    start = lb+1
    end = ub

    while True:
        while array[start] <= pivot and start <= end:
            start = start + 1 #start eke index ek wadi wenva
        while array[end] > pivot and start <= end:
            end = end -1   #end eke agaya adu index ekt env

        if start<end: # start eke index wada end eke index ek wadinm
            array[start],array[end] = array[end],array[start] # swap karanav

        else:
            break

    array[lb],array[end] = array[end],array[lb] #finaly pivot  end ekth ekk ewap karnv
    return end

def quickSort(array,start,end):
    if start >= end: #end ekt wda starat ek vishalanm mokuth karn na  return krnva
        return

    k = partition(array,start,end)
    quickSort(array,)
