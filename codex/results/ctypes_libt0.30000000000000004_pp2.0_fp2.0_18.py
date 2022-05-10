import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
#1 = OK | 2 = OK/Cancel | 3 = Abort/Retry/Ignore | 4 = Yes/No/Cancel | 5 = Yes/No | 6 = Retry/Cancel
#16 = Critical Message icon | 32 = Warning Query icon | 48 = Warning Message icon | 64 = Information Message icon
#0 = Default icon | 256 = Stop Message icon | 512 = Question Message icon | 768 = Warning Message icon | 1024 = Information Message icon
#4 = OK/Cancel | 5 = Yes/No | 6 = Yes/No
#16384 = Right Align | 32768 = RTL Reading
#0 = Default | 4096 = Application Modal | 8192 = System Modal | 65536 = Task Modal
#0 = Default | 1048576 = Topmost | 2097152 = Right | 4194304 = Bottom | 8388608 = Left

#MessageBox(0, "Your text", "Your title", 1)
#MessageBox(0, "Your text", "Your title", 1 | 16)
#MessageBox(
