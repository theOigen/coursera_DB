import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix, i, j, value = record
    for n in range(5):
        if matrix == 'a':
            cell = (i, n)
            col_row = j
        else:
            cell = (n, j)
            col_row = i
        mr.emit_intermediate(cell, (matrix, col_row, value))


def reducer(key, list_of_values):
    matrix_a = [(item[1], item[2]) for item in list_of_values if item[0] == 'a']
    matrix_b = [(item[1], item[2]) for item in list_of_values if item[0] == 'b']

    result = 0

    for item_a in matrix_a:
        for item_b in matrix_b:
            if item_a[0] == item_b[0]:
                result += item_a[1] * item_b[1]

    if result != 0:
        mr.emit((key[0], key[1], result))

    # Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
