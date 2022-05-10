import ctypes
ctypes.windll.user32.SetProcessDPIAware()
PROCNAME = "obs64.exe"

def handleFound(handle):
    print ("\n[*] %d ==>\t"  %handle)
    print ("[+] Process Name\t: " + GetNameByHandle(handle))
    print ("[+] Process ID\t: " + GetPIDByHandle(handle))
    print ("[+] Path\t\t: "+GetPathByHandle(handle))
    print ("[+] Device Path\t: " + repr(GetDevicePath(handle)))
    print ("[+] Type Name\t: " + str(GetTypeName(handle)))
    print ("[+] Descriptor\t: " + GetDescriptorByHandle(handle))
    print ("[+] Display Name\t: " + GetDisplayNameByHandle(handle))
    print ("[+] Access\t: " + hex(GetAccessByHandle(handle)))
    print ("[+] Object name\t: " + str(GetObjectNameByHandle(handle)))
    print ("
