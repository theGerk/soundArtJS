#!/bin/sh

sleep 20

#navigate to folder
cd /home/pi/soundArtJS

#pull any updates
git pull

#RUN THE PROGRAM!!! :D
python3 bathroomNoise.py
