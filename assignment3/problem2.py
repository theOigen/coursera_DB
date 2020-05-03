import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

orders = []

def mapper(record):
    id = record[1]
    mr.emit_intermediate(id, record)

def reducer(key, list_of_values):
    order = []
    for record in list_of_values:
        if record[0] == "order":
            order = record
        elif record[0] == "line_item":
            mr.emit(order + record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
