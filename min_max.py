import pandas as pd

training_data_converted_new = pd.read_csv("training_data_converted_new.csv", header=None)
# print training_data_converted_new

min = training_data_converted_new.iloc[:, [3]].min()
print min
max = training_data_converted_new.iloc[:, [3]].max()
print max

min1 = training_data_converted_new.iloc[:, [4]].min()
print min1
max1 = training_data_converted_new.iloc[:, [4]].max()
print max1