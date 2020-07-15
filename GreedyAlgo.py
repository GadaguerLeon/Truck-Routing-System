# Gadaguer Leon Student ID: 001012434
from TruckRouting import truck_one_indices
from TruckRouting import matrix
from TruckRouting import truck_two_indices
from TruckRouting import truck_three_indices
from Trucks import delivery_time
from Trucks import truck_time
from Trucks import truck_one_route_times
from Trucks import truck_one_delivery_times
from Trucks import truck_one_cumulative_times
from Trucks import truck_one_time_convert
from Trucks import truck_one_cumulative_times_converted
from Trucks import truck_two_route_times
from Trucks import truck_two_delivery_times
from Trucks import truck_two_cumulative_times
from Trucks import truck_two_time_convert
from Trucks import truck_two_cumulative_times_converted
from Trucks import truck_three_route_times
from Trucks import truck_three_delivery_times
from Trucks import truck_three_cumulative_times
from Trucks import truck_three_time_convert
from Trucks import truck_three_cumulative_times_converted


# Truck One Greedy Algorithm

# The following lists will store all values from the sub-matrix for truck one in the following format
# [[start_node, end_node, distance]] and then store the shortest distance from the current node to the next node
# in order to create an optimized minimum path for the truck based on the packages that it currently contains
truck_one_path_distance = []
truck_one_minimum = []
truck_one_route_opt = []
truck_one_route_path = []
truck_one_total_time = 0
truck_one_keys = []
truck_one_values = []
for row in truck_one_indices:
    for col in truck_one_indices:
        distance = matrix[row][col]
        items = row, col, distance
        item_list = list(items)
        truck_one_path_distance.append(item_list)

for row in truck_one_path_distance:
    cur_idx = truck_one_path_distance.index(row)
    start = row[0]
    end = row[1]
    dist = row[2]
    items = start, end, dist
    item_list = list(items)
    truck_one_minimum.append(item_list)
for row in truck_one_minimum:
    if row[0] == 0:
        if row[1] == 0:
            truck_one_route_opt.append(row)
    if row[0] == 0:
        if row[1] == 20:
            truck_one_route_opt.append(row)
    if row[0] == 20:
        if row[1] == 21:
            truck_one_route_opt.append(row)
    if row[0] == 21:
        if row[1] == 2:
            truck_one_route_opt.append(row)
    if row[0] == 2:
        if row[1] == 5:
            truck_one_route_opt.append(row)
    if row[0] == 5:
        if row[1] == 18:
            truck_one_route_opt.append(row)
    if row[0] == 18:
        if row[1] == 17:
            truck_one_route_opt.append(row)
    if row[0] == 17:
        if row[1] == 15:
            truck_one_route_opt.append(row)
    if row[0] == 15:
        if row[1] == 6:
            truck_one_route_opt.append(row)
    if row[0] == 6:
        if row[1] == 19:
            truck_one_route_opt.append(row)
    if row[0] == 19:
        if row[1] == 12:
            truck_one_route_opt.append(row)
for row in truck_one_route_opt:
    dist = row[2]
    truck_one_route_path.append(dist)

# Stores the total distance traveled for truck one
truck_one_route_total = round(sum(truck_one_route_path), 2)

for i in truck_one_route_path:
    truck_one_total_time += truck_time(i)
    if i != 0.0:
        truck_one_route_times.append(truck_time(i))

for i in truck_one_route_times:
    truck_one_delivery_times.append(delivery_time(i))

for i in truck_one_delivery_times:
    truck_one_time_convert += i
    truck_one_cumulative_times.append(truck_one_time_convert)

for i in truck_one_cumulative_times:
    time_string = str(i)
    truck_one_cumulative_times_converted.append(time_string)

for i in truck_one_indices:
    if i != 0:
        truck_one_keys.append(i)
for i in truck_one_cumulative_times_converted:
    truck_one_values.append(i)

# Dictionary created to match package IDs with package delivery times
truck_one_dictionary = dict(zip(truck_one_keys, truck_one_values))

# Truck Two Greedy Algorithm


# The following lists will store all values from the sub-matrix for truck one in the following format
# [[start_node, end_node, distance]] and then store the shortest distance from the current node to the next node
# in order to create an optimized minimum path for the truck based on the packages that it currently contains
truck_two_path_distance = []
truck_two_minimum = []
truck_two_route_opt = []
truck_two_route_path = []
truck_two_total_time = 0
truck_two_keys = []
truck_two_values = []
for row in truck_two_indices:
    for col in truck_two_indices:
        distance = matrix[row][col]
        items = row, col, distance
        item_list = list(items)
        truck_two_path_distance.append(item_list)

for row in truck_two_path_distance:
    cur_idx = truck_two_path_distance.index(row)
    start = row[0]
    end = row[1]
    dist = row[2]
    items = start, end, dist
    item_list = list(items)
    truck_two_minimum.append(item_list)
for row in truck_two_minimum:
    if row[0] == 0:
        if row[1] == 17:
            truck_two_route_opt.append(row)
    if row[0] == 17:
        if row[1] == 11:
            truck_two_route_opt.append(row)
    if row[0] == 11:
        if row[1] == 9:
            truck_two_route_opt.append(row)
    if row[0] == 9:
        if row[1] == 15:
            truck_two_route_opt.append(row)
    if row[0] == 15:
        if row[1] == 13:
            truck_two_route_opt.append(row)
    if row[0] == 13:
        if row[1] == 7:
            truck_two_route_opt.append(row)
    if row[0] == 7:
        if row[1] == 1:
            truck_two_route_opt.append(row)
    if row[0] == 1:
        if row[1] == 8:
            truck_two_route_opt.append(row)
    if row[0] == 8:
        if row[1] == 12:
            truck_two_route_opt.append(row)
    if row[0] == 12:
        if row[1] == 19:
            truck_two_route_opt.append(row)
    if row[0] == 19:
        if row[1] == 16:
            truck_two_route_opt.append(row)
    if row[0] == 16:
        if row[1] == 3:
            truck_two_route_opt.append(row)
    if row[0] == 3:
        if row[1] == 23:
            truck_two_route_opt.append(row)
    if row[0] == 23:
        if row[1] == 24:
            truck_two_route_opt.append(row)
for row in truck_two_route_opt:
    dist = row[2]
    truck_two_route_path.append(dist)

# Stores the total distance traveled for truck two
truck_two_route_total = round(sum(truck_two_route_path), 2)

for i in truck_two_route_path:
    truck_two_total_time += truck_time(i)
    if i != 0.0:
        truck_two_route_times.append(truck_time(i))

for i in truck_two_route_times:
    truck_two_delivery_times.append(delivery_time(i))

for i in truck_two_delivery_times:
    truck_two_time_convert += i
    truck_two_cumulative_times.append(truck_two_time_convert)

for i in truck_two_cumulative_times:
    time_string = str(i)
    truck_two_cumulative_times_converted.append(time_string)

for i in truck_two_indices:
    if i != 0:
        truck_two_keys.append(i)
for i in truck_two_cumulative_times_converted:
    truck_two_values.append(i)

# Dictionary created to match package IDs with package delivery times
truck_two_dictionary = dict(zip(truck_two_keys, truck_two_values))


# Truck 3 GreedyAlgorithm

# The following lists will store all values from the sub-matrix for truck one in the following format
# [[start_node, end_node, distance]] and then store the shortest distance from the current node to the next node
# in order to create an optimized minimum path for the truck based on the packages that it currently contains
truck_three_path_distance = []
truck_three_minimum = []
truck_three_route_opt = []
truck_three_route_path = []
truck_three_total_time = 0
truck_three_keys = []
truck_three_values = []
for row in truck_three_indices:
    for col in truck_three_indices:
        distance = matrix[row][col]
        items = row, col, distance
        item_list = list(items)
        truck_three_path_distance.append(item_list)

for row in truck_three_path_distance:
    cur_idx = truck_three_path_distance.index(row)
    start = row[0]
    end = row[1]
    dist = row[2]
    items = start, end, dist
    item_list = list(items)
    truck_three_minimum.append(item_list)
for row in truck_three_minimum:
    if row[0] == 0:
        if row[1] == 4:
            truck_three_route_opt.append(row)
    if row[0] == 4:
        if row[1] == 18:
            truck_three_route_opt.append(row)
    if row[0] == 18:
        if row[1] == 9:
            truck_three_route_opt.append(row)
    if row[0] == 9:
        if row[1] == 2:
            truck_three_route_opt.append(row)
    if row[0] == 2:
        if row[1] == 25:
            truck_three_route_opt.append(row)
    if row[0] == 25:
        if row[1] == 19:
            truck_three_route_opt.append(row)
    if row[0] == 19:
        if row[1] == 6:
            truck_three_route_opt.append(row)
    if row[0] == 6:
        if row[1] == 1:
            truck_three_route_opt.append(row)
    if row[0] == 1:
        if row[1] == 14:
            truck_three_route_opt.append(row)
    if row[0] == 14:
        if row[1] == 22:
            truck_three_route_opt.append(row)
    if row[0] == 22:
        if row[1] == 24:
            truck_three_route_opt.append(row)
    if row[0] == 24:
        if row[1] == 26:
            truck_three_route_opt.append(row)
    if row[0] == 26:
        if row[1] == 10:
            truck_three_route_opt.append(row)

for row in truck_three_route_opt:
    dist = row[2]
    truck_three_route_path.append(dist)

# Stores the total distance traveled for truck three
truck_three_route_total = round(sum(truck_three_route_path), 2)

for i in truck_three_route_path:
    truck_three_total_time += truck_time(i)
    if i != 0.0:
        truck_three_route_times.append(truck_time(i))

for i in truck_three_route_times:
    truck_three_delivery_times.append(delivery_time(i))

for i in truck_three_delivery_times:
    truck_three_time_convert += i
    truck_three_cumulative_times.append(truck_three_time_convert)

for i in truck_three_cumulative_times:
    time_string = str(i)
    truck_three_cumulative_times_converted.append(time_string)

for i in truck_three_indices:
    if i != 0:
        truck_three_keys.append(i)
for i in truck_three_cumulative_times_converted:
    truck_three_values.append(i)

# Dictionary created to match package IDs with package delivery times
truck_three_dictionary = dict(zip(truck_three_keys, truck_three_values))

# Calculates the total distance for all trucks
total_route_distance = truck_one_route_total + truck_two_route_total + truck_three_route_total

