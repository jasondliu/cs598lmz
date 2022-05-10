import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import os
import time
import json
from picamera import PiCamera
from datetime import datetime
from time import sleep
from azure.storage.blob import BlockBlobService, PublicAccess


while True:
    try:
        camera = PiCamera()
        camera.start_preview()
        sleep(5)
        timestamp=time.strftime("%Y%m%d%H%M%S")
        print(timestamp)
        camera.capture(timestamp + '_image.jpg')
        print("Captured")
        camera.stop_preview()
        camera.close()

        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='minio', account_key='minio123')

        # Create a container called 'quickstartblobs'.
        container_name ='camera1'
        block_blob_service.create_container(container
