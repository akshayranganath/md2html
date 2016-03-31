# md2html
Python program to convert Markdown files to HTML

## Usage
	python md2html.py <Markdown file>

###Optional Use

	python md2html.py <Markdown file> <Output HTML>

This program converts the markdown file to HTML and saves it with the same name and an HTML extension, if no output file name is provided. For help, use this: 

	python md2html.py -h
	
	usage: md2html.py [-h] [-outfile OUTFILE] infile

	Converts a markdown file to HTML

	positional arguments:
	  infile            Markdown file to convert

	optional arguments:
	  -h, --help        show this help message and exit
	  -outfile OUTFILE  HTML file name for converted file, default is
	                    <infile>.html
