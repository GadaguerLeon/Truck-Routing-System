# Gadaguer Leon Student ID: 001012434
import datetime


# The following lists will contain the packages for each truck
truck_one = []
truck_two = []
truck_three = []

# Truck speed specified by the project requirements
truck_speed = 18

# Departure times that I decided to use for each truck
truck_one_departure = '8:00:00'
truck_two_departure = '10:20:00'
truck_three_departure = '13:00:00'

# Calculated time from destination to destination will be stored in this list
truck_one_route_times = []

# Timedelta of route times will be stored in this list
truck_one_delivery_times = []

# The following list will store the cumulative sum of the delivery times starting at 8:00:00 in timedelta format
truck_one_cumulative_times = []

# The following list stores the cumulative sum of the delivery times in string format after conversion from timedelta
truck_one_cumulative_times_converted = []


# Calculated time from destination to destination will be stored in this list
truck_two_route_times = []

# Timedelta of route times will be stored in this list
truck_two_delivery_times = []

# The following list will store the cumulative sum of the delivery times starting at 8:00:00 in timedelta format
truck_two_cumulative_times = []

# The following list stores the cumulative sum of the delivery times in string format after conversion from timedelta
truck_two_cumulative_times_converted = []

# Calculated time from destination to destination will be stored in this list
truck_three_route_times = []

# Timedelta of route times will be stored in this list
truck_three_delivery_times = []

# The following list will store the cumulative sum of the delivery times starting at 8:00:00 in timedelta format
truck_three_cumulative_times = []

# The following list stores the cumulative sum of the delivery times in string format after conversion from timedelta
truck_three_cumulative_times_converted = []

# The following function will be used to calculate the time it takes to reach a destination when given distance as an
# argument
def truck_time(distance):
    travel_time = distance / truck_speed
    travel_time = round(travel_time * 3600, 2)
    return travel_time

# The following function will convert an integer into a timedelta object when given seconds as an argument
def delivery_time(n):
    return datetime.timedelta(seconds=n)


# Converts '8:00:00' to a timedelta object
(h, m, s) = truck_one_departure.split(':')
truck_one_time_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


# Converts '10:20:00' to a time delta object
(h, m, s) = truck_two_departure.split(':')
truck_two_time_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


# Converts '13:00:00' to a time delta object
(h, m, s) = truck_three_departure.split(':')
truck_three_time_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


