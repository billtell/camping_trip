
import pandas as pd
import numpy as np
import pgeocode

class Tent:

    def __init__(self, name):

        self.name = name
        self.brand = ''
        self.dimensions = ''
        self.seasons = 3,4
        self.capacity = ''
        self.style = cabin, dome

class backpack:

    def __init__(self, name):

        self.name = name
        self.brand = ''
        self.pockets = ''

class camping_location:

    def __init__(self, location);

        self.location = location
        self.longitude = ''
        self.latitude = ''
        self.climate = ''
        self.forcast = ''

    def set_latitude(self, latitude_point):
        self.latitude = latitude_point

    def set_longitude(self, longitude_point):
        self.longitude = longitude_point
