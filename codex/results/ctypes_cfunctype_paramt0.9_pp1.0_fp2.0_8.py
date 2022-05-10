import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_void_p,
    ctypes.c_void_p)

def run():
  cf = COM.CreateFrame()
  # CreateWebViewWithRequest, Make sure the url is a valid url.
  cwv = COM.CreateWebViewWithRequest(cf, COM.MakeRequest(
      'http://www.google.com'))
  func_ptr = ctypes.cast(OnLoadingFinish, FUNTYPE)
  COM.SetLoadingFinishCa
