import threading
threading._DummyThread._Thread__stop = lambda x:42
sys.setdefaultencoding("UTF-8")


def runAC(workingFolder, testIndex):
	fileName = 'ac.ac'
	if os.path.isfile(workingFolder + '/' + fileName):
		os.rename(workingFolder + '/' + fileName, workingFolder + '/' + fileName + '_old')
	os.system('bash ../runAC.sh ' + workingFolder + ' ' + fileName + ' ' + testIndex)


def genExistsInfo(workingFolder, testIndex):
	existsInfoFile = workingFolder + '/existsInfo.aci'

	file = open(existsInfoFile, 'a')
	file.write(testIndex + '\n')
	file.close()


def genTargetInfo(workingFolder, testIndex):
	targetInfoFile = workingFolder + '/targetInfo.aci'

	file = open(targetInfoFile, 'a')
	file.write(testIndex + '\n')
	file.close()


if __name
