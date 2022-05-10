import weakref
import thread

# Command sent to the timer thread to indicate that it should exit.
TIMER_STOP = -1

# Used to represent a timer that doesn't have a duration.
DO_NOT_RUN = -1

def _timer_thread(callback):
    """
    The actual callback handler.  This is run in a separate thread because it
    uses handlers that may not return promptly, which would block further
    timer dispatches.
    """
    while True:
        # Wait for the timer to fire.
        delay = callback()
        if delay == TIMER_STOP:
            # If you set the delay to TIMER_STOP, the timer stops. 
            return
        if delay == DO_NOT_RUN:
            # If the timer duration is DO_NOT_RUN, then it is a one-shot timer 
            # which has now finished.
            return
        if isinstance(delay, (int, float)):
            # If the the duration is a float or int, it indicates a periodic 
            # timer, so re-post the timer with the given
