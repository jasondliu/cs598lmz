import sys, threading

def run():
    os.system('python --version') # Add your script here

# Run thread
thread = threading.Thread(target=run)
thread.start()

# Create window
root = tk.Tk()
root.title('Tkinter Window')
root.geometry('200x100')
lbl = tk.Label(master=root, text='Hello World!')
lbl.pack()

# Run event loop
root.mainloop()
</code>
I get the following warning in the console:
<blockquote>
<p>UserWarning: Do not pass a figure to show()<br/>
The above warning is printed when I run the threads. If I don't run any threads, the warning is not printed.</p>
</blockquote>
This is strange, because I'm not doing anything related to Matplotlib nor passing anything to <code>show()</code>. It also doesn't seem to be related to Tkinter, because if I comment out
<code># Create window
root = tk.Tk()
root.title('Tkinter Window')
root.geometry('
