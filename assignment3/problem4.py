import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

friends = []

def mapper(record):
    # key: document identifier
    # value: document contents
    friends.append(record)
    name = record[0]
    friend = record[1]
    mr.emit_intermediate(friend, name)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for friend in list_of_values:
        if [key, friend] not in friends:
            mr.emit((friend, key))
            mr.emit((key, friend))

        if [friend, key] not in friends:
            mr.emit((key, friend))
            mr.emit((friend, key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
