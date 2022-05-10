import ctypes
ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
</code>
but it also doesn't work. I mean, it opens up a second terminal, but it still doesn't have admin permission.
Any other way to do this ?


A:

You can try to add a manifest to your application.
See this StackOverflow post for more information on this.
The manifest you can use looks like:
<code>&lt;?xml version="1.0" encoding="UTF-8" standalone="yes"?&gt;
&lt;assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"&gt;
  &lt;trustInfo xmlns="urn:schemas-microsoft-com:asm.v3"&gt;
    &lt;security&gt;
      &lt;requestedPrivileges&gt;
        &lt;requestedExecutionLevel level="requireAdministrator" uiAccess="false"/&gt;
      &lt;/requestedPriv
