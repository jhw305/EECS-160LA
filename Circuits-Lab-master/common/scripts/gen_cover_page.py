#!/usr/bin/python
import common
import gen_files
import sys
import os

# Arg1 : report name
# Arg2 : course
# Arg3 and above : author names

# TODO: Python docs
# TODO: Error checking

COVER_PG_SECT = "cover"

def print_usage( ) :
	print( "gen_cover_page.py" )
	print( "------------" )
	print( "Used to generate cover page of a report." )
	print( "Argument 1 - report name" )
	print( "Argument 2 - course name" )
	print( "Arguments 3 and after - author names" )
	print( "Example usage: " )
	print( "gen_cover_page.py \"We Are 138\" \"EECS 170B\" \"Glenn Danzig\" \"Jerry Only\" \"Manny Martinez\"" )
	print( "Run \"gen_cover_page.py -test\" for a test of the program" )

# report_name :: string with the name of the report
# course :: string with the name of the course
# authors :: list of strings of the author names
def cover_page_txt( report_name , course , authors ) :
	txt = ""
	txt += "\centering" + common.NEWLINE
	txt += "\\vspace*{5cm}" + common.NEWLINE
	txt += "{\huge " + report_name + " \par}" + common.NEWLINE
	txt += "{\Large " + course + " \par}" + common.NEWLINE
	txt += "{\Large \\today \par}" + common.NEWLINE
	txt += "\\vspace{1cm}" + common.NEWLINE
	for author_name in authors :
		txt += "{\large " + author_name + " \par}" + common.NEWLINE
	txt += "\\vspace{1cm}" + common.NEWLINE
	return txt

def cover_page_wrap( ) :
	txt = ""
	txt += "\documentclass{article}" + common.NEWLINE
	txt += "\input{../preamble.tex}" + common.NEWLINE
	txt += "\\begin{document}" + common.NEWLINE
	txt += "\\begin{titlepage}" + common.NEWLINE
	txt += "\\input{" + gen_files.content_fname( COVER_PG_SECT ) + "}" + common.NEWLINE
	txt += "\\end{titlepage}" + common.NEWLINE
	txt += "\\end{document}" + common.NEWLINE
	return txt

def gen_cover_page_files( report_name , course , authors ) :
	# TODO Check to ensure no file conflicts occur
	# TODO Make a cover_page dir and fname macro and update all these files later, like gen_main.py
	cover_page_dir = "cover_page"
	os.makedirs( cover_page_dir )
	# generate wrap file
	with open( "./" + cover_page_dir + "/" + gen_files.wrap_fname( COVER_PG_SECT ) , common.WRITE ) as wrap_handle :
		wrap_handle.write( cover_page_wrap( ) )
	# generate cover page file
	with open( "./" + cover_page_dir + "/" + gen_files.content_fname( COVER_PG_SECT ) , common.WRITE ) as content_handle :
		content_handle.write( cover_page_txt( report_name , course , authors ) )
	# generate Makefile
	with open( "./" + cover_page_dir + "/" + gen_files.MAKEFILE , common.WRITE ) as makefile_handle :
		makefile_handle.write( gen_files.gen_makefile_txt( COVER_PG_SECT ) )

if __name__ == "__main__" :
	if len( sys.argv ) <= 1 :
		print_usage( )
	elif len( sys.argv ) > 1 and len( sys.argv ) < 4 :
		print( "Wrong number of arguments. Use no arguments for usage." )
	else:
		report_name = sys.argv[ 1 ]
		course = sys.argv[ 2 ]
		authors = sys.argv[ 3: ]
		gen_cover_page_files( report_name , course , authors )
