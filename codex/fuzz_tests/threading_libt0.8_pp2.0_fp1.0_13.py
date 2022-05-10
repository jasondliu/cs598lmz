import threading
threading.stack_size(2**27)

class Mote(object):
    def __init__(self, mote_id, position, number_of_cycles, cycle_length, interevent_time, radius, sensitivity):
        self.id = mote_id
        self.position = position
        self.number_of_cycles = number_of_cycles
        self.cycle_length = cycle_length
        self.interevent_time = interevent_time
        self.radius = radius
        self.sensitivity = sensitivity
        self.is_activated = True

    def compute_transmission_start_time(self, cycle_time, time_offset):
        """
        Compute transmission start time for each cycle
        :param cycle_time: cycle time
        :param time_offset: time offset of cycle
        :return: List of transmission start time for each cycle
        """
        transmission_start_time_list = []
        for i in range(0, self.number_of_cycles):
            transmission_start_time = cycle_time * i + time_offset
           
