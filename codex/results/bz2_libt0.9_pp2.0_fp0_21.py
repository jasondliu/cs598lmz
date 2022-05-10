import bz2
bz2.hello

import tarfile
print tarfile.open('code.tar.gz').extractall('.')

# Create a tar file
# import tarfile
# new_tar = tarfile.open("new.tar", "w")
# new_tar.add("newdir")
# new_tar.close()

# Compress a tar file
# import tarfile
# tar = tarfile.open("code.tar.gz", "w:gz")
# for name in ["code.tar", "code2.tar", "code3.tar"]:
#     tar.add(name)
# tar.close()

# Add files to compressed tar file
# import tarfile
# tar = tarfile.open("code.tar.gz", "a:gz")
# for name in ["code.tar", "code2.tar", "code3.tar"]:
#     tar.add(name)
# tar.close()
