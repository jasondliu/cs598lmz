import threading
# Test threading daemon by preventing process from exiting
someThread = threading.Thread(target=lambda x: None, args=(None,), daemon=True)
someThread.start()

# Get the number of ZFS filesystems
child = subprocess.Popen(['zfs', 'list','-H'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = child.communicate()
y = str(out).split('\\n')
#print(y)
# Initialize arrays
zfs_array = []
dr_array = []
# Import the configuration data and read into an array
with open('/etc/snapraid.conf', 'r') as config:
    data = config.readlines()

# Loop through the array and remove blanks
for x in data:
    if not (x.split() == []):
        zfs_array.append(x)
#print(zfs_array)

# Pull the name of the data array from configuration file
data = zfs_array[0].split(' ')
#print(zfs_array
