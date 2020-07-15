# Gadaguer Leon Student ID: 001012434
import csv
from HashTable import HashMap
from Trucks import truck_one
from Trucks import truck_two
from Trucks import truck_three


# The CSV file has been modified to exclude the original labels for the data and only contains the values needed
with open('WGUPS Package File.csv') as package_csv:
    package_data = csv.reader(package_csv, delimiter=',')

    # The following code creates a Hashmap object using the imported Hashmap class
    package_hash_map = HashMap()

    # The for loop iterates through the rows of data from the WGUPS Package File. Each row from the data file is
    # treated as a list and the index/column values are stored as variables corresponding to the data contained within
    # the cell
    for row in package_data:
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip = row[4]
        delivery_time_frame = row[5]
        package_weight = row[6]
        package_note = row[7]
        package_start = ''
        package_location = ''
        package_delivery_time = ''
        package_status = 'Currently at hub'
        # The above values will be stored in the package_data_values so that they can all be stores as one value into
        # the Hash Map using the insert function from HashTable.py
        package_data_values = [package_id, package_address, package_city, package_state, package_zip,
                               delivery_time_frame, package_weight, package_note, package_start, package_location,
                               package_delivery_time, package_status]
        # Under the assumption that Package IDs are unique I decided to use them as the keys for the hash map
        key = package_id
        value = package_data_values

        # Every package that does not have to be delivered by the end of the day will be treated with priority and
        # loaded onto truck_one
        if value[5] != 'EOD':
            # Some of the packages with delivery times contain package notes specifying that the packages must be
            # delivered with 'certain package', are delayed, or contain no notes. Packages that must be delivered
            # with 'certain package' or don't have any notes will be loaded onto truck_one as long as the truck has
            # less than 16 packages
            if 'Must be delivered with' in value[7] or not value[7]:
                if len(truck_one) < 16:
                    truck_one.append(value)

        # Packages that contain 'Delayed' within the package notes will be loaded onto truck_two as long as the truck
        # has less than 16 packages
        if 'Can only be on truck' in value[7] or 'Delayed' in value[7]:
            if len(truck_two) < 16:
                truck_two.append(value)

        # Any package that contains 'wrong address listed' within the package notes will be have the correct address
        # updated and will then be loaded onto truck_two as long as the truck has less than 16 packages
        if 'Wrong address listed' in value[7]:
            value[1] = '410 S State St'
            value[4] = '84111'
            if len(truck_two) < 16:
                truck_two.append(value)

        # Any package that hasn't been loaded onto any truck will be loaded onto truck_three until the number of
        # of packages on truck_three is equal to or greater than the packages on truck_two and will then be loaded onto
        # truck_two
        if value not in truck_one and value not in truck_two and value not in truck_three:
            if len(truck_three) < len(truck_two):
                truck_three.append(value)
            else:
                truck_two.append(value)
        package_hash_map.insert(key, value)


def get_package_hash_map():
    return package_hash_map


def truck_one_package_list():
    return truck_one


def truck_two_package_list():
    return truck_two


def truck_three_package_list():
    return truck_three

# Used the commented code below for debugging in order to make sure that there were a total of 40 packages and no
# duplicates loaded onto the trucks
#
# print(len(truck_three) + len(truck_two) + len(truck_one))
#
# print(len(truck_three))
# print(len(truck_two))
# print(len(truck_one))
# duplicate = []
# for row in truck_one:
#     duplicate.append(row[0])
# for row in truck_two:
#     duplicate.append(row[0])
# for row in truck_three:
#     duplicate.append(row[0])
# for i in range(0, len(duplicate)):
#     duplicate[i] = int(duplicate[i])
# print(sorted(duplicate))
