#!/usr/bin/python

from phue import Bridge
import logging
import random

logging.basicConfig()
b = Bridge('10.1.4.158')

light_names = b.get_light_objects('name')

for light in ["Jenny's Room"]:
  light_names[light].on = False

