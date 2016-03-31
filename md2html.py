import argparse

def find_anchor_tags(line):
	recursion = False

	index = line.find('[')
	if index != -1 and line.find(']') > -1:
		if line[index-1] != '!':						
			#this is not an image tag
			if len(line.split('[')) > 2:				
				recursion = True				
			
			#remove one link at a time
			(before, line) = line.split('[',1)
			(alt, line) = line.split('](',1)
			(link,after) = line.split(')',1)			
			line = before + '<a href="' + link +'">' + alt + '</a>' + after
				
			if recursion:
				line = find_anchor_tags(line)

	return line


def convert(infile, outfile):
	
	if outfile is None:
		outfile = infile.split('.md')[0] + '.html'		

	try:
		f = open(infile)	
		w = open(outfile, 'w')
	except IOError as e:
		print 'Unable to proceed *** '+ str(e)
		return 
	

	w.write('''<html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><head><title>Testing Code</title><style>
body	{color: black; font-family: Arial, sans-serif, serif}
h1,h2,h3 	{color: rebeccapurple;}
</style>
</head><body>
''')

	pre = 0
	blockquote = 0

	for line in f:		
		# first handle for <pre></pre> tags
		if(line.startswith('   ') ):
			if pre == 0:
				w.write('<pre>')
				pre = 1
				w.write(line)
			else:
				w.write(line)
		elif line.startswith('>') :
			if blockquote == 0:
				w.write('<blockquote>')
				blockquote = 1
				w.write( line.strip('>') )
			else:
				w.write( line.strip('>') )
		else:
			if pre == 1:
				w.write( '</pre>' )
				pre = 0
			if blockquote == 1:
				w.write('</blockquote>')
				blockquote = 0
		
			line = line.strip()
			# now run the link check
			line = find_anchor_tags(line)

			if(line.startswith("#")):
				if(line.startswith("###")):
					w.write("<h3>" + line.split('###')[1] + "</h3>")
				elif(line.startswith("##")):
					w.write("<h2>" + line.split('##')[1] + "</h2>")
				elif(line.startswith("#")):
					w.write("<h1>" + line.split('#')[1] + "</h1>")
			else:
				#check if it is an image
				if( line.find("<img ") > -1):
					w.write(line)
				elif( line.startswith('![') ):
					#image tag
					(alt, link) = line.split('![')[1].split(']')
					link = link.strip('(').strip(')')
					w.write("<img style=\"float: right;\" src=\""+ link + "\" alt=\"" + alt + "\" />")
				else:			
					w.write("<p>" + line + "</p>")	
	
	w.write("</body></html>")
	f.close()
	w.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Converts a markdown file to HTML")
	parser.add_argument("infile", help="Markdown file to convert")
	parser.add_argument("-outfile", help="HTML file name for converted file, default is <infile>.html")
	args = parser.parse_args()
	print 'Converting ' + args.infile + 'to HTML..'	
	convert(args.infile, args.outfile)
	print 'Done.'

