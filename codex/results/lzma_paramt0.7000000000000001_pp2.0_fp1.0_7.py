from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)
</code>


A:

I've found the solution.
The problem was that I was using the default installation of python 3.8, without any other libraries or frameworks.
Once I've installed Anaconda and created a new environment using the following command:
<code>conda create -n myenv python=3.8 anaconda
</code>
And then I activated the environment using the command:
<code>conda activate myenv
</code>
I was able to run the script without any problem.

