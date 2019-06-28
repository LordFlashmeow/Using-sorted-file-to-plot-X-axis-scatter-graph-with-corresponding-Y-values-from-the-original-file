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


runs = []

file_0 = {}
file_1 = {}
file_2 = {}

for result in us_csv_file:
    node_name = result[0]
    node_value = result[1]

    if file_0.get(node_name):   # If the node exists in the list
        file_0[node_name].append(node_value)
    else:
        file_0[node_name] = [node_value]

runs.append(file_0)

for result in us_csv_file1:
    node_name = result[0]
    node_value = result[1]

    if file_1.get(node_name):   # If the node exists in the list
        file_1[node_name].append(node_value)
    else:
        file_1[node_name] = [node_value]

runs.append(file_1)

for result in us_csv_file2:
    node_name = result[0]
    node_value = result[1]

    if file_2.get(node_name):   # If the node exists in the list
        file_2[node_name].append(node_value)
    else:
        file_2[node_name] = [node_value]

runs.append(file_2)


# all_plots = [[[], []],[[], []],[[], []]]

all_plots = [] # Make an array of 3 arrays, each with a pair of arrays inside
# Each pair holds the x and y coordinates of the datapoints

for x in range(3):
    all_plots.append([[],[]])


for run_number, run_group in enumerate(runs):

    for key, values in run_group.items():
        sorted_position = csv_file.index(key)
        for item in values:
            all_plots[run_number][0].append(sorted_position)
            all_plots[run_number][1].append(int(item))

#indicates the label names at the given spot
plt.legend(loc='upper right')

#Creates grid for x-y axises
plt.grid(True)

#Creates wrapped title for the graph
plt.title("\n".join(wrap("longlonglonglonglonglonglonglonglonglonglonglonglonglongTITLETITLETITLETITLETITLETITLE")),size = 9.5)

#x-y labels for the graph
plt.xlabel("Node Names", fontsize = 8)
plt.ylabel("Run Times", fontsize = 8)


plt.scatter(all_plots[0][0], all_plots[0][1], c='b', marker='+', label="First")
plt.scatter(all_plots[1][0], all_plots[1][1], c='g', marker=(5,2), label="Second")
plt.scatter(all_plots[2][0], all_plots[2][1], c='r', marker=(5,1), label="Third")


#ticks - x and y axisses' data format.

plt.xticks(range(len(csv_file))[::25], [item for item in csv_file][::25], rotation=90, size=8)


plt.yticks(np.arange(0,11000,1000), size=8)

#Saves a PNG file of the current graph to the folder and updates it every time
plt.savefig('./test.png', bbox_inches='tight')

# Not to cut-off bottom labels(manually) - enlarges bottom
plt.gcf().subplots_adjust(bottom=0.23)


plt.show()
