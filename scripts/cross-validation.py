import sys
import random
import os
import math

# Split data randomly into training/testing sets

config_template = """\
classes=2
train={}
valid={}
names=data/sharks.names
backup=backup/"""

data_file = sys.argv[1]
num_sets = int(sys.argv[2])
divide = 0.5

with open(data_file) as f:
    filenames = f.readlines()

filenames = list(filter(lambda x: x != "\n", filenames))

basename = os.path.splitext(data_file)[0]
train_datasets = []
test_datasets = []
for i in range(num_sets):
    new_set = filenames.copy()
    random.shuffle(new_set)
    middle = math.floor(len(new_set) * divide)
    train_datasets.append(new_set[:middle])
    test_datasets.append(new_set[middle:])

for i in range(num_sets):
    train_filename = "{}-train-set{}.txt".format(basename, i)
    with open(train_filename, "w") as f:
        f.writelines(train_datasets[i])

    test_filename = "{}-test-set{}.txt".format(basename, i)
    with open(test_filename, "w") as f:
        f.writelines(test_datasets[i])

    config_filename = "{}-set{}.data".format(basename, i)
    with open(config_filename, "w") as f:
        f.write(config_template.format(train_filename, test_filename))
