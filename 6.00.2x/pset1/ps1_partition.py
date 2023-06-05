#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

for item in (get_partitions(['a','b','c','d'])):
     print(item)
     
medic = {'Boo': 20, 'Miss Bella': 25, 'Milkshake': 40, 'MooMoo': 50, 'Lotus': 40, 'Horns': 25}
medic = {'Boo': 20, 'Miss Bella': 25, 'Milkshake': 40}

def cows(medic):
    for item in (get_partitions(medic.items())):
        yield item
     
alistofnum = []
total = 0
brute_force = []
for item in get_partitions(medic.items()):
    brute_force.append(item)
    # alistofnum.append(total)
    # total = 0
    # for cow in item:
    #     for number in cow:
    #         total += number[1]
    
def brute(cows,limit=10):
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