import matplotlib.pyplot as plt
import numpy as np

min_num = 0
max_num = 10
number_data = 100

range = max_num - min_num
s = np.random.uniform(min_num,max_num,number_data).astype(int)
plt.xlabel('VALUE')
plt.ylabel('FREQUENCY')
count, bins, ignored = plt.hist(s, range , density=True)
plt.plot(bins, np.full_like(bins,range/number_data), linewidth=2, color='r')
plt.show()
print(s)