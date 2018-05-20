#!/usr/bin/python

# https://github.com/studioimaginaire/phue
# https://docs.python.org/2/library/random.html

from phue import Bridge
import logging
import random

logging.basicConfig()
b = Bridge('10.1.4.158')

light_names = b.get_light_objects('name')

for light in ["Jenny's Room", "Bathroom"]:
#for light in ["Study 1", "Study 2", "Study 3", "Study 4"]:

  state = random.random() < 0.8
  #state = True
  light_names[light].on = state

  if state:
    # brightness [ 0 - 255 ]
    # saturation [ 0 - 255 ]
    # hue        [ 0 - 65535 ]
    light_names[light].brightness = random.randint(50,255)
    light_names[light].hue = random.randint(3500,55000);
    light_names[light].saturation = random.randint(0,255);
