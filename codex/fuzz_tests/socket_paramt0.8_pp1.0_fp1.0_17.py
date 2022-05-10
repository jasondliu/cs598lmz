import socket
socket.if_indextoname(3)

sp.SystemInformation.GetVersion()
sp.SystemInformation.GetSystemVersion()
sp.SystemInformation.Is64bitOperatingSystem()
sp.SystemInformation.GetPlatformName()
sp.SystemInformation.GetOperatingSystemName()
sp.SystemInformation.GetComputerName()

sp.SystemInformation.GetPhysicalMemory()

# sp.SystemInformation.GetOSVersion()
# sp.SystemInformation.GetMachineName()
# sp.SystemInformation.GetUserName()
# sp.SystemInformation.GetProcessorCount()
# sp.SystemInformation.GetProcessorClockFrequency()
# sp.SystemInformation.GetPhysicalMemory()
# sp.SystemInformation.GetDiskSpace()
# sp.SystemInformation.GetDiskSpace()
# sp.SystemInformation.GetDotNetVersion()
# sp.SystemInformation.GetIPAddress()
# sp.SystemInformation.GetMACAddress()

print(sp.SystemInformation.GetDateTime())
print(sp.SystemInformation.GetDateTime().GetDate())
print(sp.SystemInformation.GetDateTime().GetTime())
