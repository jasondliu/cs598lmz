from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
CreationError:
<blockquote>
<p>Could not create an instance of class _bz2.BZ2Decompressor.</p>
<p>It is possible that you are missing a required dependency or
  combination of dependencies. </p>
<p>The original exception was: DLL load failed: The specified module could
  not be found.</p>
</blockquote>
I'm running Python 3.5.1 in a virtualenv on Windows 7.
I found this similar question, but there's not enough context to discern whether it's relevant.
What else can I try?


A:

It turns out that this error was caused by a missing Visual C++ Redistributable Package.  The one I was missing is x64, but you can verify whether this is your problem by installing it.

