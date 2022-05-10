import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
</code>
The only thing is, <code>SetCurrentProcessExplicitAppUserModelID()</code> requires a longer app-id string than our current one. That's fine, but it means we need to add a release-number to the end of the AppUserModelID string.
We currently have to do this for many assemblies and we'd like to automate it. Is there a way to replace the existing value of a <code>&lt;Assembly: Application(...)&gt;</code> at compile time with the output from a utility (that queries the project version) + the output from another utility (that maintains a revision counter) in order to build an AppUserModelID for our executables?


A:

From the comments:
<code>&lt;Assembly: Application(name="SomeName")&gt;
</code>
You want to make the name be SomeName_version.
So you want this assembly to be built and use the <code>version</code> file that contains a string of the current version (
