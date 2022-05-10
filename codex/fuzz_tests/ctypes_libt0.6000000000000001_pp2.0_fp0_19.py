import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
C++:
<code>#include &lt;Windows.h&gt;

int main()
{
    MessageBox(NULL, "Your text", "Your title", MB_OK);
}
</code>

