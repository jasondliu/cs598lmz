import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Win10VolumeMixer")

# Define a function that should be called in order to switch audio devices.
def switch_audio_devices(device_id):
    audio_devices = IAudioEndpointVolume._out_ports
    for device in audio_devices:
        if device.id == device_id:
            device.activate()

# Create an instance of the Win10VolumeMixer class.
mixer = Win10VolumeMixer()

# Register the switch_audio_devices function as a callback.
mixer.register_audio_device_switcher(switch_audio_devices)

# Run the application.
mixer.run()
</code>

