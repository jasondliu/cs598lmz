# CodeGPT
* run.py: Run the pretrained models to generate code
* tests/: Contains some code snippets that crash Python, found from bugs.python.org

# Codex
* codex.py: generate tests via Codex (requires an API key)
* unique.py: copy all unique tests in a directory to another directory
* run.py: run the generated tests and record the results in `output`
* process.py: post-process `output` based on seed input
* minimize.py: run basic linewise delta-debugging to minimize tests.

Note that `minimize.py` does not always seem to completely minimize tests.
This is probably a bug in dividing the subsets of lines for odd numbers, or
when two lines must be deleted together (e.g., an if-statement) but they
happen to end up in different subsets.
