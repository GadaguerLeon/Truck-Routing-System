# Gadaguer Leon Student ID: 001012434
from GreedyAlgo import total_route_distance
from GreedyAlgo import truck_one_dictionary
from GreedyAlgo import truck_two_dictionary
from GreedyAlgo import truck_three_dictionary
from TruckLoading import get_package_hash_map
from Trucks import truck_one_departure
from Trucks import truck_two_departure
from Trucks import truck_three_departure


print('Hello! My name is Gadaguer Leon Student ID: 001012434\n\n'
      'Welcome to my package tracking system for C950 Data Structures & Algorithms II\n')
print('Current route was completed in', total_route_distance, 'miles.\n')
user_input = input("If you would like search for an individual package please type 'lookup'. "
                   "If you would like to check the delivery status of all packages at a certain time "
                   "please type 'all'\n>")

# The following if statement will ask the user to input a package ID as well as a time.
# If the users chooses to lookup an individual package the program will get the package ID
# from the dictionary that corresponds to the truck that the package is on. Once the package has
# been located the program will then compare the time the user input to the time that the package
# will be delivered in order to update the package status
if user_input == 'lookup':
    lookup_input = int(input('Enter a package ID:\n>'))
    time_input = input('Please enter a time (HH:MM:SS) in 24-hour format:\n>')
    package_status = ''
    package_truck = ''
    if lookup_input in truck_one_dictionary:
        delivery_time = truck_one_dictionary[lookup_input]
        package_truck = 'Truck one'
        if time_input <= truck_one_departure:
            package_status = 'Currently at hub'
        elif truck_one_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'

    elif lookup_input in truck_two_dictionary:
        delivery_time = truck_two_dictionary[lookup_input]
        package_truck = 'Truck two'
        if time_input <= truck_two_departure:
            package_status = 'Currently at hub'
        elif truck_two_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'
    elif lookup_input in truck_three_dictionary:
        delivery_time = truck_three_dictionary[lookup_input]
        package_truck = 'Truck three'
        if time_input <= truck_three_departure:
            package_status = 'Currently at hub'
        elif truck_three_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'
    else:
        print('Package ID does not exist')

    print('Package', lookup_input, 'delivery information:\n',
          'Delivery address:',
          get_package_hash_map().get(str(lookup_input))[1],
          get_package_hash_map().get(str(lookup_input))[2],
          get_package_hash_map().get(str(lookup_input))[3],
          get_package_hash_map().get(str(lookup_input))[4],
          '\n',
          'Package weight:', get_package_hash_map().get(str(lookup_input))[6], 'lbs'
          '\n',
          'Delivery deadline:', get_package_hash_map().get(str(lookup_input))[5],
          '\n',
          'Delivery status:', package_status,
          '\n',
          'Delivery time:', delivery_time,
          '\n',
          'Delivered by:', package_truck)


# The following elif statement is similar to the one above. Except, rather than asking the user for the package ID, the
# program only asks for a time. Once the time has been given the program will iterate through items in the dictionary of
# each truck in order to return the status of all packages.
elif user_input == 'all':
    time_input = input('Please enter a time (HH:MM:SS) in 24-hour format:\n>')
    package_status = ''
    package_truck = ''
    for item in truck_one_dictionary:
        delivery_time = truck_one_dictionary[item]
        package_truck = 'Truck one'
        if time_input <= truck_one_departure:
            package_status = 'Currently at hub'
        elif truck_one_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'
        print('Package', item, 'delivery information:\n',
              'Delivery address:',
              get_package_hash_map().get(str(item))[1],
              get_package_hash_map().get(str(item))[2],
              get_package_hash_map().get(str(item))[3],
              get_package_hash_map().get(str(item))[4],
              '\n',
              'Package weight:', get_package_hash_map().get(str(item))[6], 'lbs'
              '\n',
              'Delivery deadline:', get_package_hash_map().get(str(item))[5],
              '\n',
              'Delivery status:', package_status,
              '\n',
              'Delivery time:', delivery_time,
              '\n',
              'Delivered by:', package_truck)

    for item in truck_two_dictionary:
        delivery_time = truck_two_dictionary[item]
        package_truck = 'Truck two'
        if time_input <= truck_two_departure:
            package_status = 'Currently at hub'
        elif truck_two_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'
        print('Package', item, 'delivery information:\n',
              'Delivery address:',
              get_package_hash_map().get(str(item))[1],
              get_package_hash_map().get(str(item))[2],
              get_package_hash_map().get(str(item))[3],
              get_package_hash_map().get(str(item))[4],
              '\n',
              'Package weight:', get_package_hash_map().get(str(item))[6], 'lbs'
              '\n',
              'Delivery deadline:', get_package_hash_map().get(str(item))[5],
              '\n',
              'Delivery status:', package_status,
              '\n',
              'Delivery time:', delivery_time,
              '\n',
              'Delivered by:', package_truck)
    for item in truck_three_dictionary:
        delivery_time = truck_three_dictionary[item]
        package_truck = 'Truck three'
        if time_input <= truck_three_departure:
            package_status = 'Currently at hub'
        elif truck_three_departure < time_input < delivery_time:
            package_status = 'In transit'
        elif time_input >= delivery_time:
            package_status = 'Delivered'
        print('Package', item, 'delivery information:\n',
              'Delivery address:',
              get_package_hash_map().get(str(item))[1],
              get_package_hash_map().get(str(item))[2],
              get_package_hash_map().get(str(item))[3],
              get_package_hash_map().get(str(item))[4],
              '\n',
              'Package weight:', get_package_hash_map().get(str(item))[6], 'lbs'
              '\n',
              'Delivery deadline:', get_package_hash_map().get(str(item))[5],
              '\n',
              'Delivery status:', package_status,
              '\n',
              'Delivery time:', delivery_time,
              '\n',
              'Delivered by:', package_truck)
else:
    print('Invalid input')
    exit()