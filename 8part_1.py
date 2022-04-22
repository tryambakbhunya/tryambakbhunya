import time
from numpy import random
import matplotlib.pyplot as plt


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

def medians_of_median(arr, l, r, k, p):
	
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

		# If position is same as k
		if (pos - l == k - 1):
			return arr[pos]
		if (pos - l > k - 1): # If position is more,
							# recur for left subarray
			return medians_of_median(arr, l, pos - 1, k,p)

		# Else recur for right subarray
		return medians_of_median(arr, pos + 1, r,k - pos + l - 1,p)

	# If k is more than the number of
	# elements in the array
	return float('inf')

trivial_partition = (3,5,7)
dataSets = {'uniform' : random.uniform , 'normal' : random.normal}

plt.figure(figsize=(16,5))

for e,key in enumerate(dataSets):
	x = []
	time_complexity = {3: [], 5: [],7: []}
	for i in range(1,5001,1000):
		arr = dataSets[key](size = i)
		x.append(i)
		mid = i//2
		for j in trivial_partition:
			start_time = time.time()
			MoM = medians_of_median(arr,0,i-1,mid,j)
			end_time = time.time()
			time_taken = end_time - start_time
			time_complexity[j].append(time_taken)

	plt.subplot(1,2,e+1)
	plt.title(key)
	plt.xlabel('Size')
	plt.ylabel('Time')
	plt.rcParams["figure.autolayout"] = True
	plt.plot(x,time_complexity[3],'r',label = 'Size : 3')
	plt.plot(x,time_complexity[5],'g',label = 'Size : 5')
	plt.plot(x,time_complexity[7],'b',label = 'Size : 7')
	plt.legend(loc='best')

plt.show()