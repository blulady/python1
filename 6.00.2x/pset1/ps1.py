###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    cowscopy = cows.copy()
    cowscopy = sorted(cowscopy.items(), key = lambda x: x[1], reverse = True)
    cows2 = cows.copy()
    cows2 = sorted(cows2.items(), key = lambda x: x[1], reverse = True)

    while cowscopy != []:
        trip = []
        changing_limit = limit
        for cow in cows2:
            if cow in cowscopy:
                if changing_limit - cow[1] >= 0:
                    trip.append(cow[0])
                    changing_limit = changing_limit - cow[1]
                    cowscopy.remove(cow)
        trips.append(trip)
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    """ one for loop walking through to pull out a cow and add it to the trip
    another loop that walks through and grabs the cow after the cow the first list
    grabbed and adds it to a different trip I then compare which is more and keep that
    trip. then i move on to the next cow, add it to list and then the other loop grabs
    the cow after that to add it to the list
    pass"""
        ## Generate set of partitions
    possible_combinations = []
    for partition in get_partitions(cows.keys()):
        possible_combinations.append(partition)
    possible_combinations.sort(key=len)

    valid_combinations = possible_combinations[:] ## or list.copy() if using python 3.3+

    ## Remove invalid partitions
    for partition in possible_combinations:
        for trip in partition:
            total = sum([cows.get(cow) for cow in trip])
            if total > limit:
                valid_combinations.remove(partition)
                break

    ## Return valid partition of minimum length
    return min(valid_combinations, key=len)
    
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


