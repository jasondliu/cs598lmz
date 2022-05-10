import lzma
lzma.LZMAError: Cannot allocate memory
</code>
I am running this on a Macbook Pro with 16GB of RAM.
I have tried to increase the memory limit using <code>ulimit -S -s unlimited</code> but it doesn't seem to have any effect.
I have also tried to run the script with <code>sudo</code> but it doesn't seem to make any difference.
I have also tried to run the script using <code>python3</code> instead of <code>python</code> but it doesn't seem to make any difference.
I have also tried to run the script using <code>python3 -m pip install lzma</code> but it doesn't seem to make any difference.
I have also tried to run the script using <code>python3 -m pip install lzma --user</code> but it doesn't seem to make any difference.
I have also tried to run the script using <code>python3 -m pip install lzma --user --upgrade</code> but it doesn't seem to make any difference.
I have also tried to run the script using <code>python3
