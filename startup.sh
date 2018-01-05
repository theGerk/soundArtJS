#!/bin/sh

#sleep 20 seconds to wait for interent connection
sleep 20

#navigate to folder
cd /home/pi/soundArtJS

#pull any updates
git pull

#RUN THE PROGRAM!!! :D
python3 bathroomNoise.py
