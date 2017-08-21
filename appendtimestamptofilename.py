import os,time
import shutil
import datetime



def get_user_input():
	'''Get user's input for the source and destination path'''

	source = raw_input('Enter the absolute path of the source directory: ')
    # Check if the directory exists
	if ((os.path.exists(source) == True)):
		return source
	else:
		print("Invalid source directory passed as input")


def append_files(source):
	'''Append file creation time stamp to filenames in the directory'''
	files = (os.listdir(source))
	for i in files:
		'''Get the file creation time stamp'''

		# check if the listing is a file or directory
		if (os.path.isfile(source + "/" + i)):
			# use os.path.getctime to get the file creation timestamp in milliseconds(long)
			# formatted the timestamp using datetime
			creation_time = datetime.datetime.fromtimestamp(os.path.getctime(source + "/" + i)).strftime('%Y-%m-%d__%H:%M:%S')

			# fetch the file extension
			filename, file_extension = os.path.splitext(source + "/" + i)
			new_name = filename + creation_time + file_extension

			# Rename the files
			os.rename(source + "/" + i,new_name)
		
	print "Done"
	return



try:
	user_input = get_user_input()
except:
	print "Did not get any valid inputs"
	exit()
append_files(user_input)
