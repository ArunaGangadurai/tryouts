import os,time
import shutil


def get_user_input():

	'''Get user's input for the source and destination path'''

	source = raw_input('Enter the absolute path of the source directory: ')
	dest   = raw_input('Enter the absolute path of the destination directory: ')

	# Check if the directory exists
	if (((os.path.exists(source) == True) and  (os.path.exists(dest) == True))):
		return [source,dest]
	else:
		print("Invalid inputs")


def move_files(source,dest):
	files = (os.listdir(source))
	for i in files:
		'''Get the file creation time stamp'''
		creation_time = os.path.getctime(source + "/" + i)
		try:
			if (os.path.isfile(source + "/" + i)):                                   # check if its a file or not
				if (int(time.time()) - int(creation_time)) > 604800:             # 604800 - no of milliseconds in a week 
					shutil.move(source + "/" + i , dest)  
					print ("file moved successfully" ,i)                     # if the files are aged enough, move them to a different directory
				else:
					print ("Not a week old to be moved ")
		except:
			print ("Unexpected Error occured. Please check the destination directory input.")

	print "Done"
	return



try:
	user_input = get_user_input()
except:
	print "Did not get any valid inputs"
	exit()
move_files(user_input[0],user_input[1])
