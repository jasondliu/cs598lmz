import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Device():
  def __init__(self, device, verbose=False):
    # If a device object is passed in, just use that
    if isinstance(device, Rock64):
      self.device = device
    # Otherwise, assume it's a serial port
    else:
      self.device = Rock64(device)
    self.verbose = verbose

  def reset_filesystem(self):
    # Make sure we're in the root directory
    self.device.cd('/')
    # We can't remove the root directory in one go, so remove the
    # contents first
    self.device.rm('-rf', '*')
    # Now remove the root
    self.device.rm('-rf', '/*')

  def upload_assets(self, assets_dir):
    # First, reset the filesystem
    self.reset_filesystem()
    # Now upload the assets
    self.device.upload_dir(assets_dir)

  def start_service(self,
