#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# solve = data.reshape((1, len(data) * len(data[0])))[0]
# max_value = sorted(solve, reverse=True)[0]
# print max_value
#
# for item in data_dict:
#     if data_dict[item]['bonus'] == max_value:
#         print item  # the answer is crazy

for item in data_dict:
    if data_dict[item]["bonus"] != 'NaN' and data_dict[item]["salary"] != 'NaN':
        if data_dict[item]["bonus"] > 5e6 and data_dict[item]["salary"] > 1e6:
            print item
