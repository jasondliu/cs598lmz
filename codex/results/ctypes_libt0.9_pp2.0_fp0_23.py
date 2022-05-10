import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Obtaining the current working directory (`cwd`)
import os
cwd = os.getcwd()
print('Your current working directory is {}'.format(cwd))

# Setting the staging directory based on `cwd`
staging_dir = cwd + '\\staging'

# Checking whether staging directory already exists, and if not, creating it
if os.path.exists(staging_dir):
	print('The staging directory already exists.')
else:
	os.mkdir(staging_dir)
	print('Created staging directory.')

# Staging directory path, and temporary file path
staging_dir_path = os.path.join(cwd, staging_dir)
temp_file_path = os.path.join(staging_dir, 'temp.csv')

# Output directory path, and output file path
output_dir_path = os.path.join(cwd, 'output')
output_file_path = os.path
