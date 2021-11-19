import sys
from csv import reader
import json

# ERROR NUMBERS
INVALID_ARGUMENT = 1

# CSV COLUMNS
TIME_COLUMN = 1
SOURCE_COLUMN = 2
TARGET_COLUMN = 3


def calculate(call, buildings_arr, output_path):
    pass


def build_matrix(calls_path, buildings_path, output_path):
    # open file in read mode
    with open(calls_path, 'r') as calls:
        # pass the file object to reader() to get the reader object
        call_csv = reader(calls)

        # with open(buildings_path) as buildings_file:
        #     building_data = json.load(buildings_file)

        for call in call_csv:
            # calculate(call, building_data.get('_elevators'), output_path)
            


                print(call)



if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(INVALID_ARGUMENT)
    build_matrix(sys.argv[1], sys.argv[2], sys.argv[3])



