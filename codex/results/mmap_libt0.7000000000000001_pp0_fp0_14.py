import mmap
+
+
+def parse_input(lines):
+    return [int(line) for line in lines]
+
+
+def run_intcode(program):
+    """Runs an intcode program. Returns the state at the end."""
+    ip = 0
+    while True:
+        opcode = program[ip]
+        if opcode == 99:
+            break
+        else:
+            in1 = program[program[ip+1]]
+            in2 = program[program[ip+2]]
+            out = program[ip+3]
+            if opcode == 1:
+                program[out] = in1 + in2
+            elif opcode == 2:
+                program[out] = in1 * in2
+            else:
+                raise RuntimeError(f"Invalid opcode {opcode}")
+            ip += 4
+    return program
+
+
+def main():
+    with open('input.txt', 'r+') as f:
+        mm = mmap.mmap(f
