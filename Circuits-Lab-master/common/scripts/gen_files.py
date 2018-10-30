#!/usr/bin/python

import common
import os
import sys

WRAP="_wrap"
PREAMBLE_FNAME="preamble"+common.TEX_EXT
MAKEFILE="Makefile"

def print_usage( ) :
	print( "gen_files.py" )
	print( "------------" )
	print( "Used to generate directories and files for each section of a report." )
	print( "Please provide any number of arguments greater than or equal to 1." )
	print( "Each argument is the name of a section as it will appear in your document." )
	print( "Example usage: " )
	print( "gen_files.py \"How to Defend Yourself against Fresh Fruit\" \"The Spanish Inquisition\" \"Bicycle Repairman\"" )
	print( "Run \"gen_files.py -test\" for a test of the program" )

# Filename generators
def section_dirname( section_name ) :
	# TODO Need stricter rules to accomodate :'s and other misc. characters
	return section_name.lower( ).replace( " " , "_" )

def wrap_fname( section_name ) :
	return section_dirname( section_name ) + WRAP + common.TEX_EXT

def content_fname( section_name ) :
	return section_dirname( section_name ) + common.TEX_EXT

# File content generators
def gen_makefile_txt( section_name ) :
	txt = ""
	txt += "LATEX=pdflatex" + common.NEWLINE
	txt += "BUILD=$(LATEX) " + wrap_fname( section_name ) + common.NEWLINE
	txt += common.NEWLINE
	txt += "build: " + content_fname( section_name ) + " " + wrap_fname( section_name ) + common.NEWLINE
	txt += "	$(BUILD)" + common.NEWLINE
	txt += "	$(BUILD)" + common.NEWLINE
	return txt

def gen_wrap_file_txt( section_name ) :
	txt = ""
	txt += "\\documentclass{article}" + common.NEWLINE
	txt +=  "\\input{../" + PREAMBLE_FNAME + "}" + common.NEWLINE
	txt +=  "\\begin{document}" + common.NEWLINE
	txt +=  "\\input{" + content_fname( section_name ) + "}" + common.NEWLINE
	txt +=  "\\end{document}" + common.NEWLINE
	return txt

# File and directory generators
# TODO Error checking to ensure that no file conflicts occur
def gen_section_dir( section_name ) :
	dirname = section_dirname( section_name )
	# Create dir
	os.makedirs( dirname )
	# Create Makefile
	with open( "./" + dirname + "/" + MAKEFILE , common.WRITE ) as makefile_handle :
		makefile_handle.write( gen_makefile_txt( section_name ) )
	# Create wrap and content files
	with open( "./" + dirname + "/" + wrap_fname( section_name ) , common.WRITE ) as wrap_handle :
		wrap_handle.write( gen_wrap_file_txt( section_name ) )
	with open( "./" + dirname + "/" + content_fname( section_name ) , common.WRITE ) as content_handle :
		content_handle.write( "" )

if __name__ == "__main__" :
	if len( sys.argv ) <= 1 :
		print_usage( )
	else :
		sections = sys.argv[ 1: ]
		for section in sections:
			gen_section_dir( section )
