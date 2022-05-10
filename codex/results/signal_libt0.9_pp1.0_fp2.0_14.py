import signal
signal.signal(signal.SIGINT, handler)

openRTSP = ["-i", "rtsp://192.168.1.29/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream",
            "-f", "segment",
            "-segment_time", "90",
            "-segment_format", "mp4",
            "-segment_list", "index.m3u8",
            "-segment_list_size", "10",
            "-segment_list_type", "m3u8",
            "-map", "0",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "64k",
            "-ar", "48000",
            "-bsf:a", "aac_adtstoasc",
            "-hls_flags", "delete_segments",
            "live%d.mp4"
            ]
#live.mp4

while(shouldContinue):
    #get video stream
   
