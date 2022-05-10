import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# setup some basic vars
serverProfile = "default"
serverName = "Default"
serverPort = 3478
serverIP = ""
serverPassword = ""

# setup some advanced vars
serverMaxPlayers = 32

# setup some advanced vars
serverMaxPlayers = 32
serverGameMode = 0
serverMapName = "mp_dome"
serverMaxSpectators = 0
serverMapList = [serverMapName]
serverGamePassword = ""
serverGamePasswordSpectators = ""
serverGamePasswordPrivate = ""
serverGamePasswordPrivateSpectators = ""
serverPunkBuster = False
serverPunkbusterKey = "abcdefghijklmnopqrstuvwxyz0123456789"
serverPunkbusterVersion = ""
serverPunkbusterAutoUpdate = False
serverHardcore = False
serverHitIndicator = True
serverCrosshair = True
server3dSpotting = True
serverMiniMap = True
server3pCam = True
serverTeamBalance = False
serverBannerUrl = ""
