# Gadaguer Leon Student ID: 001012434
import csv
from TruckLoading import truck_one_package_list
from TruckLoading import truck_two_package_list
from TruckLoading import truck_three_package_list


with open('WGUPS Distance Table.csv') as distance_table:
    read_distance = csv.reader(distance_table, delimiter=',')
    read_distance = list(read_distance)

with open('Destination Name Data.csv') as destination_name:
    destination_name_data = csv.reader(destination_name, delimiter=',')
    destination_name_data = list(destination_name_data)

    # The following for loop converts the string values within the 2D array float values
    for i in range(len(read_distance)):
        for j in range(len(read_distance[i])):
            read_distance[i][j] = float(read_distance[i][j])

    # Final matrix created form the WGUPS Distance Table file
    matrix = read_distance

    # In order to create a route for a truck a new list is created from the current packages on the truck
    # without duplicate addresses
    truck_one_package_list = truck_one_package_list()
    truck_one_route = []

    truck_two_package_list = truck_two_package_list()
    truck_two_route = []

    truck_three_package_list = truck_three_package_list()
    truck_three_route = []

    # The following lists will store the indices(destinations) that will be needed to build the routes for each
    # truck based on the packages that are currently loaded.
    truck_one_indices = [0]
    truck_two_indices = [0]
    truck_three_indices = [0]

    # Route creation for truck_one
    for row in truck_one_package_list:
        destination = row[1]
        if destination not in truck_one_route:
            truck_one_route.append(destination)

    # Route creation for truck_two
    for row in truck_two_package_list:
        destination = row[1]
        if destination not in truck_two_route:
            truck_two_route.append(destination)

    # Route creation for truck_three
    for row in truck_three_package_list:
        destination = row[1]
        if destination not in truck_three_route:
            truck_three_route.append(destination)

    # Once the route for truck_one has been created the following for loop is used in order to match the destination
    # address for the packages on the truck to the index from the WGUDistanceNameData file and it is then appended to
    # the list of indexes needed for truck_one to pull from the matrix
    for row in destination_name_data:
        temp = row[2]
        for i in truck_one_route:
            if i in temp:
                truck_one_indices.append(int(row[0]))

    # Indices needed for truck_two
    for row in destination_name_data:
        temp = row[2]
        for i in truck_two_route:
            if i in temp:
                truck_two_indices.append(int(row[0]))

    # Indices needed for truck_three
    for row in destination_name_data:
        temp = row[2]
        for i in truck_three_route:
            if i in temp:
                truck_three_indices.append(int(row[0]))

