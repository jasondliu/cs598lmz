import select
import json
import os
import re

class FlightPlan(object):
    """
    This class models a flight plan.
    """
    
    def __init__(self, flight_plan_name):
        """
        Construct a flight plan.
        """
        self.flight_plan_name = flight_plan_name
        self.flight_plan_file = 'flight_plans/' + flight_plan_name + '.json'
        if not os.path.isfile(self.flight_plan_file):
            print("Unable to find the flight plan file '" + self.flight_plan_file + "'")
            exit(-1)

        # Open the flight plan file and read it all in.
        f = open(self.flight_plan_file, 'r')
        self.flight_plan_data = json.load(f)
        f.close()

        # Validate the flight plan.
        if not self.validate():
            print("Flight plan '" + self.flight_plan_file + "' failed validation.")
            exit(-1)

        #
