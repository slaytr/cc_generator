import matplotlib.pyplot as plt
import numpy as np

# with open("average_ratios.txt", "r") as f:
#     np.loadtxt()
#     file = f.readlines()
#     ratios = []
#     for line in file:
#         ratios.append(line.split(',')[0])
#     print(ratios)
data = np.loadtxt('average_ratios3.txt', delimiter=",",usecols=(0))

print(data.min(), data.max(), data.mean(), len(data))

n, bins, patches = plt.hist(x=data, color='#0504aa', bins=np.arange(data.min(), data.max(),0.1))

plt.xlabel('Ratio')
plt.ylabel('Frequency')
plt.title('A Frequency Plot of the Average Contrast Ratios of Randomly Generated 10-Colour Groups (100,000 Samples)')
# Set a clean upper y-axis limit.

plt.show()
