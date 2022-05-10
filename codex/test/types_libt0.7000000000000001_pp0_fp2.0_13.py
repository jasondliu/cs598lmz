import types
types.SimpleNamespace()

def is_active_room(room):
    return room.is_active and room.activity_type == room.activity_type.PLAYING

def get_active_rooms(state):
    rooms = list(filter(is_active_room, state.rooms))
    if not rooms:
        return []
    
    room = rooms[0]

    return [room]

class Session():
    def __init__(self, state):
        self.state = state
        self.room = None
        self.timer = None
        self.is_running = False
        self.reconnect_timer = None
        self.message_queue = []

    def is_active(self):
        return self.room is not None and self.room.is_active

    def start(self):
        self.is_running = True
        self.reconnect_timer = Timer(300, self.start)
        self.reconnect_timer.start()

