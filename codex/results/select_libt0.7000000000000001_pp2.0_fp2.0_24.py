import select
import pyinotify


def inotify_events(wd, name, mask, process_events=True):
    """Helper function to process inotify events."""
    # print("IN_MODIFY", name, mask, wd)
    # print("MASK_OPEN", name, mask, wd)
    # print("MASK_CLOSE_NOWRITE", name, mask, wd)
    # print("MASK_CLOSE_WRITE", name, mask, wd)
    if mask & pyinotify.IN_MODIFY:
        print("FILE MODIFIED:", name, mask, wd)
    if mask & pyinotify.IN_CLOSE_WRITE:
        print("FILE CLOSED:", name, mask, wd)
    if mask & pyinotify.IN_MOVED_TO:
        print("FILE MOVED TO:", name, mask, wd)
    if mask & pyinotify.IN_MOVED_FROM:
        print("FILE MOVED FROM:", name, mask, wd)
   
