import lzma
lzma.LZMAError

# Bump version based on last tag
import subprocess
proc = subprocess.Popen('git describe --tags', stdout=subprocess.PIPE, shell=True)
(output, err) = proc.communicate()
gitVers = output.strip()
gitVers = gitVers[1:]
print(gitVers)
proc = subprocess.Popen('git shortlog HEAD ^%s' % gitVers, stdout=subprocess.PIPE, shell=True)
(output, err) = proc.communicate()
gitMsg = output.strip()
if gitMsg == b"":
    gitMsg = b"No new commits since tag"

version = str(gitVers, "utf-8")
print("Last tag: %s" % version)

GIT_VERSION = version.split("-g")[0]+ ".dev" + version.split("-g")[1].replace("-", "")

VERSION_TEXT = '''\
#define IDS_VERSION_STRING "%s"
#define IDS_VERSION_NUMBER "%
