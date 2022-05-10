import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PushaT's Acrylic")

AcrylicPath = os.environ["LOCALAPPDATA"] + "\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

def Acrylic(id):
     """
     This function will download an image from the Acrylic Path,
     and will get the image with specified IDs
     """
     AcrylicFile = requests.get(f"ms-appx:///Assets/{id}.jpg", stream=True)
     fileName = f"{id}.jpg"

     with open(fileName, 'wb') as f:
          for chunk in AcrylicFile:
               f.write(chunk)
     filePath = os.path.abspath(fileName)

     return filePath


if not os.path.isdir(AcrylicPath):
    print('An error has occured.\nYour Windows might not be supported.')
    sys.exit(0)

fileNames = os.listdir(AcrylicPath
