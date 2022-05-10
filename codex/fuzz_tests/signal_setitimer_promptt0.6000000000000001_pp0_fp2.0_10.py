import signal
# Test signal.setitimer() by calling signal.setitimer() several times
# with different values.
import signal
import time

setitimer_args = [
    # alarm, value, initial_alarm
    (0.1, 0.1, 0.1),
    (0.2, 0.2, 0.2),
    (0.3, 0.3, 0.3),
    (0.4, 0.4, 0.4),
    (0.5, 0.5, 0.5),
    (0.6, 0.6, 0.6),
    (0.7, 0.7, 0.7),
    (0.8, 0.8, 0.8),
    (0.9, 0.9, 0.9),
    (1.0, 1.0, 1.0),
    (1.1, 1.1, 1.1),
    (1.2, 1.2, 1.2),
    (1.3, 1.3, 1.3),
    (1.4, 1.4, 1.4),
    (
