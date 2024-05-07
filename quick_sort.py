def partition(array, lb, ub):
    pivot = array[lb]
    start = lb+1
    end = ub

    while True:
        while array[start] <= pivot and start <= end:
            start = start + 1 #start eke index ek wadi wenva
        while array[end] > pivot and start <= end:
            end = end -1   #end eke agaya adu index ekt env

        #uda 2km wel natahara unt pasee check karala abalana index ek ,
        # start ekt vada end eke index eke wadida kiyla
        if start<end: # start eke index wada end eke index ek wadinm
            array[start],array[end] = array[end],array[start] # swap karanav

        else:
            break

    array[lb],array[end] = array[end],array[lb] #finaly pivot  end ekth ekk ewap karnv
    return end

def quickSort(array,start,end):
    if start >= end: #end ekt wda starat ek vishalanm mokuth karn na  return krnva
        return

    k = partition(array,start,end) # partition function ek call karnava
    quickSort(array,start,k-1)
    quickSort(array,k+1,end)

data = [10,6,11,8,12,2,9,15]
print("Before Sorting : {}".format(data))

lb =0 #low bound eke index ek
ub = len(data)-1 # upper bound eke index ek
quickSort(data,lb,ub) # function ek call karnva

print("After Sorting : {}".format(data))

#After Sorting : [2, 6, 8, 9, 10, 11, 12, 15]