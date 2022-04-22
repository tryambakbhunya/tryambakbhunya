import numpy as np
import matplotlib.pyplot as plt
from random import randint,randrange,random
import time

uniform_distribution=[]
normal_distribution=[]

for i in range(10):
    uniform_distribution.append(np.random.uniform(low=0,high=1,size=2**i))

for i in range(10):
    normal_distribution.append(np.random.normal(0,1,2**i))

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data) + 0.001)

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b
def bucketSort(x):
    arr = []
    slot_num =10
    for i in range(slot_num):
        arr.append([])
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
def correctness(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
x_uniform = []
x_normal = []
time_complexity_uniform = []
time_complexity_normal = []

for i in uniform_distribution:
    x_uniform.append(len(i))
    # print('uniform Data Set: ', i)
    start_time = time.time()
    bucketSort(i)
    end_time = time.time()
    time_taken = end_time - start_time
    # print('Sorted Data Set: ', i)
    # print('correctness: ', correctness(i))
    time_complexity_uniform.append(time_taken)

for j in normal_distribution:
    x_normal.append(len(j))
    arr=NormalizeData(j)
    # print('Normal Data Set: ',arr)
    start_time = time.time()
    bucketSort(i)
    end_time = time.time()
    time_taken = end_time - start_time
    # print('Sorted Data Set: ',arr)
    # print('correctness: ', correctness(arr))
    time_complexity_normal.append(time_taken)

plt.xlabel('Size')
plt.ylabel('Time')
plt.plot(x_uniform, time_complexity_uniform, 'g',label='uniform')
plt.plot(x_normal, time_complexity_normal, 'r',label='normal')
print(x_normal,x_uniform)
plt.show()