User
Consider the following insertion sort algorithm:


InsertionSort(arr, n)
1. for i from 1 to n-1 do
2.     key = arr[i]
3.     j = i - 1
4.     while j >= 0 and arr[j] > key do
5.         arr[j+1] = arr[j]
6.         j = j - 1
7.     arr[j+1] = key


a) Write a Python program that reads a list of integers from the keyboard and the length of the list.
b) Develop a function in Python named insertion_sort and implement the above insertion sort algorithm.
c) Pass the input list and its length as parameters to the function developed and get the sorted list as output.
d) Use a loop to run the program and display the correct output until the user inputs -1 for the length of the list.

def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


while True:
    length = int(input("Enter the length of the list (-1 to exit): "))
    if length == -1:
        print("Exiting the program.")
        break
    if length <= 0:
        print("Length must be a positive integer.")
        continue
    arr = []
    print("Enter the elements of the list:")
    for _ in range(length):
        arr.append(int(input()))
    sorted_arr = insertion_sort(arr, length)
    print("Sorted list:", sorted_arr)

Here's a similar question using the bubble sort algorithm:

---

Consider the following bubble sort algorithm:


BubbleSort(arr, n)
1. for i from 0 to n-1 do
2.     for j from 0 to n-i-1 do
3.         if arr[j] > arr[j+1] then
4.             swap arr[j] and arr[j+1]


a) Write a Python program that reads a list of integers from the keyboard and the length of the list.
b) Develop a function in Python named bubble_sort and implement the above bubble sort algorithm.
c) Pass the input list and its length as parameters to the function developed and get the sorted list as output.
d) Use a loop to run the program and display the correct output until the user inputs -1 for the length of the list.

---

This question prompts the user to input a list of integers and its length, then sorts the list using the bubble sort algorithm. The program continues to execute until the user inputs -1 for the length of the list.


def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_integer_list():
    integer_list = []
    for i in range(length):
        num = int(input("Enter an integer (-1 to stop): "))
        if num == -1:
            break
        integer_list.append(num)
    return integer_list

while True:
    length = int(input("Enter the length of the list (-1 to stop): "))
    if length == -1:
        break

    input_list = read_integer_list()
    bubble_sort(input_list, length)
    print("Sorted list:", input_list)



Consider the following Quick Sort algorithm:


QuickSort(arr, low, high)
1. if low < high then
2.     pivot_index = Partition(arr, low, high)
3.     QuickSort(arr, low, pivot_index - 1)
4.     QuickSort(arr, pivot_index + 1, high)

Partition(arr, low, high)
1. pivot = arr[high]
2. i = low - 1
3. for j from low to high-1 do
4.     if arr[j] < pivot then
5.         i = i + 1
6.         swap arr[i] and arr[j]
7. swap arr[i+1] and arr[high]
8. return i + 1


a) Write a Python program that reads a list of integers from the keyboard and the length of the list.
b) Develop functions in Python named quick_sort and partition to implement the above Quick Sort algorithm.
c) Pass the input list, its low index (0), and high index (length - 1) as parameters to the quick_sort function, and pass additional parameters to the partition function as needed.
d) Use a loop to run the program and display the correct output until the user inputs -1 for the length of the list.

---

This question prompts the user to input a list of integers and its length, then sorts the list using the Quick Sort algorithm. The program continues to execute until the user inputs -1 for the length of the list.

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def read_integer_list():
    integer_list = []
    for i in range(length):
        num = int(input("Enter an integer (-1 to stop): "))
        if num == -1:
            break
        integer_list.append(num)
    return integer_list

while True:
    length = int(input("Enter the length of the list (-1 to stop): "))
    if length == -1:
        break
    input_list = read_integer_list()
    quick_sort(input_list, 0, length - 1)
    print("Sorted list:", input_list)



Here's a question based on the Merge Sort algorithm:

---

Consider the following Merge Sort algorithm:


MergeSort(arr)
1. if length of arr > 1 then
2.     mid = length of arr // 2
3.     left_half = arr[:mid]
4.     right_half = arr[mid:]
5.     MergeSort(left_half)
6.     MergeSort(right_half)
7.     Merge(arr, left_half, right_half)

Merge(arr, left_half, right_half)
1. i = j = k = 0
2. while i < length of left_half and j < length of right_half do
3.     if left_half[i] < right_half[j] then
4.         arr[k] = left_half[i]
5.         i = i + 1
6.     else
7.         arr[k] = right_half[j]
8.         j = j + 1
9.     k = k + 1
10. while i < length of left_half do
11.     arr[k] = left_half[i]
12.     i = i + 1
13.     k = k + 1
14. while j < length of right_half do
15.     arr[k] = right_half[j]
16.     j = j + 1
17.     k = k + 1


a) Write a Python program that reads a list of integers from the keyboard and the length of the list.
b) Develop functions in Python named merge_sort and merge to implement the above Merge Sort algorithm.
c) Pass the input list as a parameter to the merge_sort function and additional parameters as needed.
d) Use a loop to run the program and display the correct output until the user inputs -1 for the length of the list.

---

This question prompts the user to input a list of integers and its length,
then sorts the list using the Merge Sort algorithm. The program continues to execute until the user inputs -1 for the length of the list.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def read_integer_list():
    integer_list = []
    for i in range(length):
        num = int(input("Enter an integer (-1 to stop): "))
        if num == -1:
            break
        integer_list.append(num)
    return integer_list

while True:
    length = int(input("Enter the length of the list (-1 to stop): "))
    if length == -1:
        break
    input_list = read_integer_list()
    merge_sort(input_list)
    print("Sorted list:", input_list)

