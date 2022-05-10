import threading
threading.Thread(target=lambda: b.connect("192.168.0.103"), daemon=True).start()

##-----------------------------------------------------------------------------
# TODO: do we want an exception that explicitly handles connection errors?
# TODO: add constants for paths
##-----------------------------------------------------------------------------
# pitch is set by pid, rather than the output
# define pins

Pin.objects.filter(name='ElevatorOutput').update(               value=0,  max_value=100, min_value=-100)
Pin.objects.filter(name='AileronOutput').update(                value=0,  max_value=100, min_value=-100)
Pin.objects.filter(name='ThrottleOutput').update(               value=0,  max_value=100, min_value=-100)
Pin.objects.filter(name='GyroPitchOutput').update(              value=0,  max_value=100, min_value=-100)
Pin.objects.filter(name='GyroRollOutput').update(               value=0,  max_value=100, min_value=-100)
Pin.objects.filter(name
