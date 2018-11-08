
# Author: Mohammad Kamar Uddin
# Description: KNN classifier using external (batch) test data set
# Python version: 2.7.14

import csv

from data_prep import prepare_test_data, prepare_test_set_for_appending, appending
from knn_function_external_testdata import knn
from datetime import datetime

# Declaring necessary variables

test_filename = 'test_data_2k.csv' # Change the name accordingly (for future usage)
training_file = 'training_data_converted_latest.csv' # Change the name accordingly (for future usage)
min_max_file = 'min_max.csv' # Change the name accordingly (for future usage)
test_set = [] # Initialize a empty list for test instances
append_ls = [] # Initialize a empty list for prediction 

print "Process started at: ", datetime.now()

# Preparing test data set
prepare_test_data(test_filename, test_set)

# Applying KNN to test data set
knn_classifier_result = knn(test_set, training_file, min_max_file)

# Preparing list to append predicted values to generate new file
prepare_test_set_for_appending(test_filename, append_ls)

# Creating list of test instance with predicted value
new_data_set = appending(append_ls, knn_classifier_result)

# Creating a new csv file and writing the data
# Change the name if necessary
new_file = open('test_data_final_with_class_2k.csv', "wb")
writer = csv.writer(new_file, delimiter=",")

for row in new_data_set:
    writer.writerow(row)

new_file.close()

print "Process finished at: ", datetime.now()




