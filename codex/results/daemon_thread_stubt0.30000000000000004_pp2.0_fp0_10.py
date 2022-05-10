import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

threading.Thread(target=run).start()

from IPython.display import clear_output

for i in range(5):
    clear_output()
    print(i)
    time.sleep(0.5)

# %%
# %load_ext memory_profiler

# %%
# %memit range(1000000)

# %%
# %mprun -f range range(1000000)

# %%
# %load_ext line_profiler

# %%
# %lprun -f range range(1000000)

# %%
# %load_ext cython

# %%
# %%cython

# %%
# %load_ext snakeviz

# %%
# %snakeviz range(1000000)

# %%
# %load_ext watermark

# %%
# %watermark -v -m -p numpy,scipy,sklearn
