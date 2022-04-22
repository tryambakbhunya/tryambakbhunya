# Python implementation QuickSort using
# Lomuto's partition Scheme.
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math

def quicksort(arr, start , stop):
    if(start < stop):
        
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex,operations = partitionrand(arr,start, stop)
        
        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        operations += quicksort(arr , start , pivotindex-1)
        operations += quicksort(arr, pivotindex + 1, stop)
        return operations
    return 0

# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):

    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)

    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    operations = 1
    pivot = start # pivot
    # a variable to memorize where the
    i = start + 1
    
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
    
        if arr[j] <= arr[pivot]:
            operations += 2
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot,operations)

size = 4
x = list(range(1,size+1))
normal_operations = []
uniform_operations = []
normal_time = []
uniform_time = []

for i in range(1,size+1):
    n = 2**i
    normal_data_set = np.random.normal(0, 0.1, n)
    uniform_data_set = np.random.uniform(0,n,n)
    start_time = time.time()
    operationsNormal = quicksort(normal_data_set,0,n-1)
    end_time = time.time()
    time_taken = end_time - start_time
    normal_time.append(time_taken / n*math.log2(n))
    start_time = time.time()
    operationsUniform = quicksort(uniform_data_set,0,n-1)
    end_time = time.time()
    time_taken = end_time - start_time
    uniform_time.append(time_taken / n*math.log2(n))
    normal_operations.append(operationsNormal)
    uniform_operations.append(operationsUniform)
    print(n)

figure, axis = plt.subplots(1, 2)

axis[0].plot(x,normal_time,'ro-')
axis[0].plot(x,uniform_time,'go-')
# axis[0].xlabel('size : 2^n')
# axis[0].ylabel('time / n*log(n)')

axis[1].plot(x,normal_operations,'ro-')
axis[1].plot(x,uniform_operations,'go-')
# axis[1].xlabel('size : 2^n')
# axis[1].ylabel('operations')

plt.show()