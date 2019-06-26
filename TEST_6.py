from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import csv

#Opens the sorted hostnum.csv file and reads it; replaces the quotation marks.
csv_file = []
with open('hostnum.csv', 'r') as host:
    for line in host.readlines():
        line = line.replace('"', '')
        line = line.strip('\n')
        rank, value = line.split("	")
        csv_file.append(value)

#Opens the file and reads it
us_csv_file = []
with open('fileFirst.csv', 'r') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        us_csv_file.append(line)

us_csv_file1 = []
with open('fileSecond.csv', 'r') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        us_csv_file1.append(line)

us_csv_file2 = []
with open('fileThird.csv', 'r') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        us_csv_file2.append(line)

#Sorts the files using sorted file's index number - first coumn (x[0])
us_csv_file.sort(key=lambda x: csv_file.index(x[0]))
us_csv_file1.sort(key=lambda x: csv_file.index(x[0]))
us_csv_file2.sort(key=lambda x: csv_file.index(x[0]))

#scatters the symbols on the graph
plt.scatter(range(len(us_csv_file)), [int(item[1]) for item in us_csv_file], c='b', marker='+', label="First")
plt.scatter(range(len(us_csv_file1)), [int(item[1]) for item in us_csv_file1], c='g', marker=(5,2), label="Second")
plt.scatter(range(len(us_csv_file2)), [int(item[1]) for item in us_csv_file2], c='r', marker=(5,1), label="Third")

#indicates the label names at the given spot
plt.legend(loc='upper right') 

#Creates grid for x-y axises
plt.grid(True)

#Creates wrapped title for the graph
plt.title("\n".join(wrap("longlonglonglonglonglonglonglonglonglonglonglonglonglongTITLETITLETITLETITLETITLETITLE")),size = 9.5)

#x-y labels for the graph
plt.xlabel("Node Names", fontsize = 8)
plt.ylabel("Run Times", fontsize = 8)

#print(len(csv_file))
#ticks - x and y axisses' data format.
plt.xticks(np.arange(0,len(csv_file)+1)[::20], csv_file[::20], rotation=90, size=8)
plt.yticks(np.arange(0,11000,1000), size=8)

#Saves a PNG file of the current graph to the folder and updates it every time
plt.savefig('./test.png', bbox_inches='tight')

# Not to cut-off bottom labels(manually) - enlarges bottom
plt.gcf().subplots_adjust(bottom=0.23)


plt.show()
