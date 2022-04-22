import numpy as np

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
	slot_num = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

def correctness(arr):
  n = len(arr)
  for i in range(n-1):
      if arr[i] > arr[i+1]:
          return False
  return True


n = 10
arr = np.random.rand(n)
print('Data Set: ',arr)
bucketSort(arr)
print('Sorted: ',arr)
print('correctness: ',correctness(arr))