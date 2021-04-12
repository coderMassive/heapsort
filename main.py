import time
from random import randint

def max_heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

arr = []
for i in range(1000000):
  arr.append(randint(1, 1000000))

start = time.time()
heapSort(arr)
end = time.time()
print(arr)
print(f"Runtime is {(end - start)} seconds")
# about 40 seconds for 1000000 items
