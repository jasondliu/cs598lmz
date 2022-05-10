from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()
resp = requests.get(
    "https://s3.amazonaws.com/tensorflow-serving-apt/tensorflow-model-server.deb")
with open('/home/nvidia/tensorflow-model-server.deb', 'wb') as f:
    f.write(LZMADecompressor.decompress(resp.content))

!dpkg -i /home/nvidia/tensorflow-model-server.deb

!sudo systemctl disable tegrastats.service
!sudo systemctl stop tegrastats.service

!sudo systemctl enable tensorflow-model-server.service
!sudo systemctl start tensorflow-model-server.service

print("Done!")

#Run TF Serving
start_time = time.time()
!pkill tensorflow-model-server
time.sleep(5)

!nvidia-smi
!nvidia-smi | grep Default | awk '{print $3}'
!nvidia-smi --query-gpu=name,index
