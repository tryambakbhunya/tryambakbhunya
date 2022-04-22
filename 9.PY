import time
from numpy import random
import matplotlib.pyplot as plt

pivot_index = []

def swap(arr, a, b):
    arr[a],arr[b] = arr[b],arr[a]

def findMedian(arr, l, n):
    lis = arr[l:l+n]    
    # Sort the array
    lis.sort()
 
    # Return the middle element
    return lis[n // 2]
  
def partitions(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i

def medians_of_median(arr, l, r, k, p = 5, t = False):

  global pivot_index
    # If k is smaller than number of
    # elements in array
  if (k > 0 and k <= r - l + 1):
        
        # Number of elements in arr[l..r]
    n = r - l + 1

        # Divide arr[] in groups of size 5,
        # calculate median of every group
        # and store it in median[] array.
    median = []

    i = 0
    while (i < n // p):
        median.append(findMedian(arr, l + i * p, p))
        i += 1

    # For last group with less than 5 elements
    if (i * p < n):
        median.append(findMedian(arr, l + i * p, n % p))
        i += 1

    # Find median of all medians using recursive call.
    # If median[] has only one element, then no need
    # of recursive call
    if i == 1:
        medOfMed = median[i - 1]
    else:
        medOfMed = medians_of_median(median, 0,i - 1, i // 2,p)

    # Partition the array around a medOfMed
    # element and get position of pivot
    # element in sorted array
    pos = partitions(arr, l, r, medOfMed)
    if t:
      pivot_index.append(pos)
    # If position is same as k
    if (pos - l == k - 1):
        return arr[pos]
    if (pos - l > k - 1): # If position is more,
                        # recur for left subarray
        return medians_of_median(arr, l, pos - 1, k,p,t)

    # Else recur for right subarray
    return medians_of_median(arr, pos + 1, r,k - pos + l - 1,p,t)

  # If k is more than the number of
  # elements in the array
  return float('inf')



dataSets = {'uniform': random.uniform , 'normal' : random.normal}

n = 50000
mid = n//2

plt.rcParams["figure.autolayout"] = True
plt.xlabel('Recursion depth')
plt.ylabel('pivot element distance')

for e,key in enumerate(dataSets):
  x = []
  distance = []
  pivot_index = []
  arr = dataSets[key](size = n)
  medians_of_median(arr,0,n-1,mid,5,True)
  for num,i in enumerate(pivot_index):
    x.append(num+1)
    distance.append(abs(mid - i - 1))
  # print(distance)
  plt.plot(x,distance,'o',label = key)

plt.legend(loc='best')
plt.show()