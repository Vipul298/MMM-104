import csv
from collections import Counter
from pickle import EMPTY_LIST
from statistics import mean
'''new_data = "Whitehatjr"
data = Counter(new_data)
new_list = data.items()
print(new_list)
value = data.values()
print(value)'''
with open('height-weight.csv', newline = '') as f : 
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
n = len(new_data)
data = Counter(new_data)
'''total = 0
for x in new_data: 
    total+=x
print("mean/average is:"+str(total/n))'''
'''new_data.sort()
if n %2==0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
    print(n)
print("median"+str(median))'''
