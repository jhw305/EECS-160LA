#!/usr/bin/python

# Roman Parise

import common
import sys

# TODO Generalize and make n-dimensional plots?

def print_usage( ) :
	print( """
gen_plt.py
---------
Generate plot from csv file in column format:
ex:
Heading 1 , Heading 2
1.00 , 2.00
3.1 , -4
....

Arguments:
1) name of the .csv file with data points including .csv
2) name of output .png file including .png
	""" )

def generate_plt_from_csv_col_data( input_csv_fname , output_png_fname ) :
	# TODO Error checking
	csv_data = common.read_csv_cols( input_csv_fname )
	my_x_title = csv_data[ 0 ].pop( 0 )
	my_y_title = csv_data[ 1 ].pop( 0 )
	common.save_plot_xy( output_png_fname , csv_data[ 0 ] , csv_data[ 1 ] , x_axis_title = my_x_title , y_axis_title = my_y_title )

if __name__ == "__main__" :
	if len( sys.argv ) == 1 :
		print_usage( )
		sys.exit( common.SUCCESS )
	elif len( sys.argv ) != 3 :
		# TODO Replace references to this fname with a variable for indirection
		print( "gen_plt.py: Please provide only two arguments (or zero for usage)." )
		sys.exit( common.ERR_CODE )
	# TODO Check if file exists. Etc error checking
	# TODO Ensure we don't overwrite existing files
	input_csv_fname = sys.argv[ 1 ]
	output_png_fname = sys.argv[ 2 ]
	generate_plt_from_csv_col_data( input_csv_fname , output_png_fname )
	sys.exit( common.SUCCESS )
