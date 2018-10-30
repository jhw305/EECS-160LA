#!/usr/bin/python
#Jason Wang

import sys
import numpy as np
import common
import csv

# Argument 1 - name of csv (excluding .csv)
# Argument 2 - number of rows
# Argument 3+ - column name, min value, max value

DECIMAL_PRECISION = 3

arguments = len(sys.argv) - 1

# TODO Error checking
with open(sys.argv[1] + '.csv', 'w') as csvfile:
	writer = csv.writer( csvfile , quoting = csv.QUOTE_MINIMAL )

	num_elements = int(sys.argv[2])
	position = 3

	data_matrix = [ ]
	while (arguments >= position):
		min_value = int(sys.argv[position + 1])
		max_value = int(sys.argv[position + 2])
		row_list = [ ]
		if min_value != 0 or max_value != 0:
			row_values = np.linspace(min_value, max_value, num_elements)
			row_values = np.around(row_values, DECIMAL_PRECISION)
			row_list = [sys.argv[position]] + row_values.tolist()
		else:
			row_list = [sys.argv[position]] + [''] * num_elements
		data_matrix.append( row_list )
		position += 3
	data_matrix = common.transpose( data_matrix )
	for row in data_matrix :
		# TODO Write with presentable spacing in the actual file
		# TODO Also, should we have smallest to largest values or largest to smallest values?
		writer.writerow( row )
