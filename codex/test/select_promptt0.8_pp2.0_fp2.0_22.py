import select
# Test select.select (and thus poll) on Windows.
# Requires the existence of /tmp/spam.  In theory, this should be
# replaced with use of temporary files and the tempfile module.

