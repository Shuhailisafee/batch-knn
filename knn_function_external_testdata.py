import math
import csv
import operator
from datetime import datetime

# Loading and processing training dataset and min_max data
# Input: training dataset file name, min_max data file name, 2 empty list
def load_data(training_dataset_filename, min_max_data_filename, training_set=[], minmax_set=[]):
    with open(training_dataset_filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        data_set = list(lines)

        for x in range(len(data_set)):

            for y in range(13):
                data_set[x][y] = float(data_set[x][y])

            # Preparing training data for KNN
            training_set.append(data_set[x])

    with open(min_max_data_filename, 'rb') as csvfile2:
        lines1 = csv.reader(csvfile2)
        minmax_data = list(lines1)

        minmax_set.append(minmax_data[0])
        minmax_set.append(minmax_data[1])


# Distance calculation Function
def calculate_distance(instance1, instance2, length, freq_disconnect_min, freq_disconnect_max,
                       neighbouring_session_min, neighbouring_session_max):

    distance = 0
    distance_euclidean = 0

    for x in range(length):

        #  Calculate hamming distance
        if x == 2:
            if instance1[x] == instance2[x]:
                distance += 0
            else:
                distance += 2

        # calculating Euclidean distance for frequent disconnection and neighbouring session attributes
        elif x == 3:
            max_freq_disconnect = freq_disconnect_max
            min_freq_disconnect = freq_disconnect_min
            temp1 = (instance1[x] - min_freq_disconnect) / (max_freq_disconnect - min_freq_disconnect)
            temp2 = (instance2[x] - min_freq_disconnect) / (max_freq_disconnect - min_freq_disconnect)
            distance_euclidean += pow((temp1 - temp2), 2)

        elif x == 4:
            max_neighbouring_session = neighbouring_session_max
            min_neighbouring_session = neighbouring_session_min
            temp1 = (instance1[x] - min_neighbouring_session) / (max_neighbouring_session - min_neighbouring_session)
            temp2 = (instance2[x] - min_neighbouring_session) / (max_neighbouring_session - min_neighbouring_session)
            distance_euclidean += pow((temp1 - temp2), 2)

        else:
            if instance1[x] == instance2[x]:
                distance += 0
            else:
                distance += 1

    distance += math.sqrt(distance_euclidean)
    return distance


# Calculating neighbors based on distance
def get_neighbors(training_set, test_instance, k, freq_disconnect_min, freq_disconnect_max,
                  neighbouring_session_min, neighbouring_session_max):
    distances = []
    length = len(test_instance)
    for x in range(len(training_set)):
        dist = calculate_distance(test_instance, training_set[x], length, freq_disconnect_min, freq_disconnect_max,
                                  neighbouring_session_min, neighbouring_session_max)
        distances.append((training_set[x], dist))
    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors


# Selecting or making decision
def get_response(neighbors):
    class_votes = {}

    for x in range(len(neighbors)):
        response = neighbors[x][-1]

        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sorted_votes[0][0]


def knn(test_set, training_dataset_filename, min_max_data_filename):

    # Necessary variables declaration
    training_set = []
    min_max_set = []
    k_value = 3

    load_data(training_dataset_filename, min_max_data_filename, training_set, min_max_set)
    frequent_disconnect_min = float(min_max_set[0][0])
    frequent_disconnect_max = float(min_max_set[1][0])
    neighbouring_session_min = float(min_max_set[0][1])
    neighbouring_session_max = float(min_max_set[1][1])

    # Prediction list
    prediction = []

    # Generating Predictions
    for rec in range(len(test_set)):
        calculated_neighbors = get_neighbors(training_set, test_set[rec], k_value, frequent_disconnect_min,
                                             frequent_disconnect_max, neighbouring_session_min,
                                             neighbouring_session_max)
        result = get_response(calculated_neighbors)
        prediction.append(result)

        if rec == 100:
            print "{} test instance has been processed at {}".format(rec, datetime.now())
        elif rec == 1000:
            print "{} test instance has been processed at {}".format(rec, datetime.now())
        elif rec == 20000:
            print "{} test instance has been processed at {}".format(rec, datetime.now())

    return prediction
