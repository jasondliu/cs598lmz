gi = (i for i in ())
# Test gi.gi_code.co_flags
print gi.gi_code.co_flags & 0x20

# Test inlining of code.
import codeop
if codeop.compile_command("a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1; a = 1;
