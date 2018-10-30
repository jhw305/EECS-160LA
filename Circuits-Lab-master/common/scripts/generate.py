#
# LaTex main file and package generation script.
# Author: John Fritsche
# Version: 0.0.1, CrudeBrewed
#
# Date: 01/22/2018
import sys


type = raw_input('What type of report would you like generated? (170, 152, or 101): ')
Filename = raw_input('Enter a file name: ')

print 'Report for '+ type + ' is being generated...'

f = open(Filename+'.tex','w')
print >> f, '\\documentclass{article}'

packs = raw_input('Would you like to choose the packages? (y or n) ')
if (packs == 'y'):
	while packs != 'q':
		packs = raw_input('Package Name: (q to exit)')
		if (packs != 'q'):
			print >> f, '\\usepackage{'+ packs +'}'
		else:
			break;

else:
	packs = '\\usepackage{listings}'

pre = '\\input{preamble.tex}'
begDoc ='\\begin{document}'
begTi = '\\begin{titlepage}'
footers = '\\end{document}'

print >> f, pre
print >> f, begDoc
print >> f, begTi

title = 'EECS'
if (type == '170'):
	title = 'EECS 170B: Electronics II'
elif (type == '152'):
	title = 'EECS 152B: DSP Design and Lab'
elif (type == '101'):
	title = 'EECS 101: Machine Vision'
else:
	title = 'Template Document'

f.write('\\title{'+title+'}\n')

print >> f, footers
print 'Done!'
f.close()		
