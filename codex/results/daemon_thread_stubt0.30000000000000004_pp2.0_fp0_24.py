import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

from IPython.display import display, clear_output

for i in range(10):
    clear_output(wait=True)
    display(i)
    time.sleep(1)

print('Done')

# %%
from IPython.display import display, clear_output

for i in range(10):
    clear_output(wait=True)
    print(i)
    time.sleep(1)

print('Done')

# %%
from IPython.display import display, clear_output

for i in range(10):
    clear_output(wait=True)
    print(i)
    time.sleep(1)

print('Done')

# %%
from IPython.display import display, clear_output

for i in range(10):
    clear_output(wait=True)
    print(i)
    time.sleep(1
