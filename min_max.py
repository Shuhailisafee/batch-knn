import pandas as pd
import csv

data = pd.read_csv("training_data_converted_new.csv", header=None)
# print training_data_converted_new

min = data.iloc[:, 3].min()
print min
max = data.iloc[:, 3].max()
print max

min1 = data.iloc[:, 4].min()
print min1
max1 = data.iloc[:, 4].max()
print max1

a = [[min, min1],[max, max1]]
print a

with open("min_max.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(a)

