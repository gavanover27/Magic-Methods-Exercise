# read in the data from the csv file
import csv

csvfile = open(r'Documents\Repositories\Class_Work\M07\exercise-magic-methods\astronauts.csv', 'r')
astronauts = csv.DictReader(csvfile)

# create the astronaut class
class Astronaut:
    """Astronaut class"""
    def __init__(self, name, flight_hr, status):
        self._name=name
        self._flight_hr = flight_hr
        self._status = status
    
    def __str__(self):
        return ('%s, %s' %(self._name, self._status))
    
    @property
    def name(self):
        return self._name
    
    @property
    def flight_hr(self):
        return self._flight_hr
    
    @property
    def status(self):
        return self._status
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @flight_hr.setter
    def flight_hr(self, new_flight_hr):
        self._flight_hr = new_flight_hr
    
    @status.setter
    def name(self, new_status):
        self._status = new_status

    def __gt__(self,other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        return self.flight_hr > other.flight_hr
    def __eq__(self,other):
        print('__eq__ called')
        return self.flight_hr == other.flight_hr
    def __ge__(self,other):
        print('__ge__ called')
        return self.flight_hr >= other.flight_hr

# Create an empyt list to store the astronauts in
astronautsList = []

# Add each astronaut to the list with only name, flight hrs, and status
for i in astronauts:
    astronautsList.append(Astronaut(i['Name'], i['Space Flight (hr)'], i['Status']))

# Print the first astronaut
print(astronautsList[0])

# Test the __gt__, __ge__, __eq__ methods
print(astronautsList[0] > astronautsList[1])
print(astronautsList[0] >= astronautsList[1])
print(astronautsList[0] == astronautsList[1])

# Print all of the astronauts from the list
for i in astronautsList:
    print(i)