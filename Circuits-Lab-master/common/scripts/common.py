#!/usr/bin/python

# Roman Parise
# Common functions for azide flow
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

WRITE="w"
COMMA_DELIMITER=","
NEWLINE="\n"
CSV_EXT=".csv"
TEX_EXT=".tex"

ERR_CODE = -1
SUCCESS = 0

# Data processing
def perc_err( measured , theoretical ):
	return abs( ( measured - theoretical ) / theoretical )

def fmt_perc_err( measured , theoretical , prec ) :
	return fmt_perc( perc_err( measured , theoretical ) , prec )

def set_precision_str( fp_number , prec ):
	return ( ( "%." + str( prec ) + "f" ) % fp_number )

def fmt_perc( perc_as_decimal , prec ):
	return ( set_precision_str( 100 * perc_as_decimal , prec ) ) + "\%"

# TODO: Overwrites files. Is this the best way to do it?
# TODO: Error checking?
def write_csv_from_matrix( fname , matrix ):
	with open( fname , WRITE ) as file_handle:
		for row in matrix:
			str_to_write = COMMA_DELIMITER.join( [ str( element ) for element in row ] )
			file_handle.write( str_to_write + NEWLINE )

def read_csv_rows( csv_fname ) :
	# Get data in a matrix
	data_matrix = [ ]
	# TODO Maybe we can use dtype to our advantage
	reader = np.genfromtxt( csv_fname , delimiter = COMMA_DELIMITER , dtype = str )
	for row_index in range( 0 , len( reader ) ) :
		data_matrix_row = [ ]
		for col_index in range( 0 , len( reader[ row_index ] ) ) :
			if row_index == 0 :
				# Headings
				data_matrix_row.append( str( reader[ row_index ][ col_index ] ) )
			else :
				# Data
				data_matrix_row.append( float( reader[ row_index ][ col_index ] ) )
		data_matrix.append( data_matrix_row )
	return data_matrix


# TODO: Need a clean way to generate plots from rows or columns format

# TODO: Needs error checking and possibly a cleaner, more elegant solution
# Reads out a csv file into cols
# Note: Top row is reserved for headings
def read_csv_cols( csv_fname ) :
	# TODO: Temp soln. Transpose the matrix to get in column form.
	return transpose( read_csv_rows( csv_fname ) )

# TODO: Only checks rank-2 tensors. Do we care about rank-n where 0 <= n < inf?
# Matrix by our current definition is a nonempty array of nonempty arrays, all of same length.
# Ex: [ [ 1 ] , [ "lolx" ] ], [ [ 1 , "lolcatz" , 3 ] ] , [ [ 2 ] , [ -1 ] , [ 3 ] ] are all matrices.
# [ 1 ] , [ [ 1 ] , [ 2 , "hahaha" ] ] , [ [ ] , [ ] ], and [ ] are not.
def is_matrix( matrix ) :
	# Is an array
	if not isinstance( matrix , list ) :
		return False
	# Nonempty array
	if len( matrix ) == 0 :
		return False
	# By design, col_num >= 0
	col_num = -1
	for row in matrix :
		# Row is an array
		if not isinstance( row , list ) :
			return False
		# Each row must be nonempty
		if len( row ) == 0 :
			return False
		# If first row, use its number of columns as the default.
		if col_num == -1 :
			col_num = len( row )
		# If not first row, check number of columns against col_num.
		elif col_num != len( row ) :
			return False
	# Array of arrays. Arrays all have same length. Therefore, matrix.
	return True

def transpose( input_matrix ) :
	if is_matrix( input_matrix ) :
		output_matrix = [ ]
		# No errors in input_matrix[ 0 ] because matrix is nonempty by our definition.
		for col_index in range( 0 , len( input_matrix[ 0 ] ) ) :
			new_row = [ ]
			for row_index in range( 0 , len( input_matrix ) ) :
				new_row.append( input_matrix[ row_index ][ col_index ] )
			output_matrix.append( new_row )
		return output_matrix
	else :
		# TODO Replace with exceptions
		print( "Cannot take transpose of a non-matrix object." )
		sys.exit( ERR_CODE )

def save_plot_xy( fname , x_list , y_list , x_axis_title = "" , y_axis_title = "" ) :
	plt.xlabel( x_axis_title )
	plt.ylabel( y_axis_title )
	plt.plot( x_list , y_list )
	plt.savefig( fname )
	plt.clf( )

def save_plot_xy_with_best_fit_line( fname , x_list , y_list ) :
	plt.plot( x_list , y_list )
	m , b , r , p , e = stats.linregress( x_list , y_list )
	x = np.linspace( min( x_list ) , max( x_list ) , 100 * len( x_list ) )
	y = m * x  + b
	plt.plot( x , y )
	plt.savefig( fname )
	plt.clf( )

if __name__ == "__main__" :
	pass
