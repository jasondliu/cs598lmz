import lzma
lzma.open
</code>
<blockquote>
<p>AttributeError: module 'lzma' has no attribute 'open'</p>
</blockquote>
<code>import pylzma
pylzma.open
</code>
<blockquote>
<p>AttributeError: module 'pylzma' has no attribute 'open'</p>
</blockquote>
I have tried using python 3.4.4 and 3.5.2.
I have tried compiling pylzma from here and here.
I have tried installing from pip (<code>pip install pylzma</code>).
I have tried installing from wheel (<code>python -m pip install pylzma‑0.4.8‑cp34‑cp34m‑win_amd64.whl</code>).
I have tried installing from wheel (<code>python -m pip install pylzma‑0.4.8‑cp35‑cp35m‑win_amd64.whl</code>).
<blockquote>
<p>ERROR: Could not install packages due to an EnvironmentError: [
