import numpy as np

def swap(arr, a, b):
    arr[a],arr[b] = arr[b],arr[a]

def findMedian(arr, l, n):
    lis = arr[l:l+n]    
    # Sort the array
    lis.sort()
 
    # Return the middle element
    return lis[n // 2]
  
def partition(arr, l, r, x):
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

def medians_of_median(arr, l, r, k):
	
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
		while (i < n // 5):
			median.append(findMedian(arr, l + i * 5, 5))
			i += 1

		# For last group with less than 5 elements
		if (i * 5 < n):
			median.append(findMedian(arr, l + i * 5,
											n % 5))
			i += 1

		# Find median of all medians using recursive call.
		# If median[] has only one element, then no need
		# of recursive call
		if i == 1:
			medOfMed = median[i - 1]
		else:
			medOfMed = medians_of_median(median, 0,
								i - 1, i // 2)

		# Partition the array around a medOfMed
		# element and get position of pivot
		# element in sorted array
		pos = partition(arr, l, r, medOfMed)

		# If position is same as k
		if (pos - l == k - 1):
			return arr[pos]
		if (pos - l > k - 1): # If position is more,
							# recur for left subarray
			return medians_of_median(arr, l, pos - 1, k)

		# Else recur for right subarray
		return medians_of_median(arr, pos + 1, r,
						k - pos + l - 1)

	# If k is more than the number of
	# elements in the array
	return float('inf')

for i in range(10,10000,1000):
  arr = np.random.uniform(1,100,i).astype(int)
  mid = i//2
  print(medians_of_median(arr,0,i-1,mid))
  print(findMedian(arr,0,i-1))