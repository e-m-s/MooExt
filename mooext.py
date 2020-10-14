# Python script - get files from Moodle ZIP archive
import sys # due to command-line arguments
import re # regular expression
import zipfile # zip archives
#import unidecode # remove diacritics
## install: "pip install unidecode" first!
import unicodedata # remove diacritics

def remove_diacritics(input_str):
	result = unicodedata.normalize('NFKD', input_str)
	result = result.encode('ASCII', 'ignore')
	result = result.decode('utf-8')
	return result


def main(argv):
	if len(sys.argv) == 0:
		print('Usage: mooext file.zip')
		exit(2)

	# Get list of all directories
	zipfilename = argv[1];
	print('Extracting task solutions from Moodle ZIP file: '+zipfilename);
	with zipfile.ZipFile(zipfilename, 'r') as myzip:
		filelist = myzip.namelist()
		for file in filelist:
			blocks = re.match("([^_/]*) ([^_/ ]*)_[^/]*/.*\.(.*)", file)
			parts = blocks.groups();
			newname = parts[1]+"_"+parts[0]+"."+parts[2]
			newname = newname.lower()
			newname = remove_diacritics(newname)
			print('* '+newname)
			output = open(newname, "wb")
			output.write(myzip.read(file)) 
			output.close()

		
main(sys.argv)