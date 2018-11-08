
import csv

filename = 'TrainingSet_new.csv'  # Change the file name accordingly (for future usage)

# Reading from csv

with open(filename, 'rb') as csvfile:
    lines = csv.reader(csvfile)
    data_set = list(lines)
    print data_set[0]
    temp_test_set = data_set[1:] # Excluding header from csv

    for x in range(len(temp_test_set)):

        for y in range(13):
            if temp_test_set[x][y] == 'Active':
                temp_test_set[x][y] = float(1)
            elif temp_test_set[x][y] == 'Tos' or temp_test_set[x][y] == 'TOS':
                temp_test_set[x][y] = float(0)
            elif temp_test_set[x][y] == 'Online':
                temp_test_set[x][y] = float(1)
            elif temp_test_set[x][y] == 'Offline':
                temp_test_set[x][y] = float(2)
            elif temp_test_set[x][y] == 'Captive':
                temp_test_set[x][y] = float(3)
            elif temp_test_set[x][y] == 'Enabled':
                temp_test_set[x][y] = float(1)
            elif temp_test_set[x][y] == 'Disabled':
                temp_test_set[x][y] = float(2)
            elif temp_test_set[x][y] == 'Good':
                temp_test_set[x][y] = float(1)
            elif temp_test_set[x][y] == 'Bad':
                temp_test_set[x][y] = float(2)
            else:
                temp_test_set[x][y] = float(temp_test_set[x][y])

# Creating a new csv file and writing the data
new_file = open('training_data_converted_new.csv', "wb")
writer = csv.writer(new_file, delimiter=",")

for row in temp_test_set:
    writer.writerow(row)

new_file.close()
