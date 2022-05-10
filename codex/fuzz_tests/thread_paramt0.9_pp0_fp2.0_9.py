import sys, threading
threading.Thread(target=lambda: sys.stderr.write("Recording in background"), daemon=True).start()
print("Flush in foreground")

# 3. Recursive Garbage Collection
# Credit: Raymond Hettinger

def gc_cycle(remaining=3):
    if remaining:
        # Explicitly call another cycle, with one less recursion
        remaining -= 1
        gc_cycle(remaining)

gc_cycle()

# 4. Generate integers in the range [0,n)

def in
