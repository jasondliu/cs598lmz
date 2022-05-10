import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
# No gesture present
POSE_NONE = 0
# Gesture present
POSE_ACTIVE = 1
# Hand    Side    Gesture
# ----    ----    -------
# Open        Left        Fist
# ----        ----        -------
# Open        Right        Thumb
# Open        Right        Index
# Closed    Right        Index
# Closed    Right        Middle
# Closed    Right        Ring
# Open        Right        Ring
# Open        Right        Pinky
# ----        ----        -------
# Closed    Left        Fist
# Open        Left        Lasso
# Open        Left        OK
# Open        Left        Vulcan
# ----        ----        -------
# Open        Either    Open
# Closed    Either    Closed


class LeapTrackerManager(pyglet.event.EventDispatcher):
    """
    Convenience class controlling one or more Leap Motion cameras,
    providing gesture and hand tracking events to a pyglet app
    """

