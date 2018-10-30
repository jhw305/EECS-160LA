#!/usr/bin/python

import common
import gen_files
import sys

MAIN = "main"

def print_usage( ) :
	print( "gen_main.py" )
	print( "------------" )
	print( "Used to generate main files for a report." )
	print( "Please provide any number of arguments greater than or equal to 1." )
	print( "Each argument is the name of a section as it will appear in your document." )
	print( "Example usage: " )
	print( "gen_main.py \"Heart-Shaped Box\" \"Smells Like Teen Spirit\" \"Lithium\"" )
	print( "Run \"gen_main.py -test\" for a test of the program" )

# section_name :: string of the section name
def section_source( section_name ) :
	txt = ""
	txt += "\section{" + section_name + "}" + common.NEWLINE
	txt += "\input{./" + gen_files.section_dirname( section_name ) + "/" + gen_files.content_fname( gen_files.section_dirname( section_name ) ) + "}" + common.NEWLINE
	return txt

# sections :: list of strings of section names
def gen_main_txt( sections ) :
	txt = ""
	txt += "\documentclass{article}" + common.NEWLINE
	txt += "\usepackage[letterpaper, portrait, margin = 1in]{geometry}" + common.NEWLINE
	txt += "\input{" + gen_files.PREAMBLE_FNAME + "}" + common.NEWLINE
	txt += "\\begin{document}" + common.NEWLINE
	txt += "\\begin{titlepage}" + common.NEWLINE
	txt += "\\input{./cover_page/cover.tex}" + common.NEWLINE
	txt += "\end{titlepage}" + common.NEWLINE
	for sect in sections :
		txt += section_source( sect )
	txt += "\end{document}" + common.NEWLINE
	return txt

def gen_main_makefile_txt( ) :
	txt = ""
	txt += "LATEX=pdflatex" + common.NEWLINE
	txt += "BUILD=$(LATEX) " + gen_files.content_fname( MAIN ) + common.NEWLINE
	txt += common.NEWLINE
	txt += "build: " + gen_files.content_fname( MAIN ) + common.NEWLINE
	txt += "	$(BUILD)" + common.NEWLINE
	txt += "	$(BUILD)" + common.NEWLINE
	return txt

def gen_main_files( sections ) :
	# TODO May have a problem with relative paths later. What if we're not in the directory where the main files should be created?
	# generate main file
	with open( gen_files.content_fname( MAIN ) , common.WRITE ) as main_handle :
		main_handle.write( gen_main_txt( sections ) )
	# generate Makefile
	with open( gen_files.MAKEFILE , common.WRITE ) as makefile_handle :
		makefile_handle.write( gen_main_makefile_txt( ) )
	# generate preamble
	with open( gen_files.PREAMBLE_FNAME , common.WRITE ) as preamble_handle :
		preamble_handle.write( "" )

if __name__ == "__main__" :
	if len( sys.argv ) <= 1 :
		print_usage( )
	else :
		sections = sys.argv[ 1: ]
		# TODO Fix. We don't want main_wrap.tex in there.
		gen_main_files( sections )
