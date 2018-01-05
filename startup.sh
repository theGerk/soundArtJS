#!/bin/sh

#navigate to folder
cd /home/pi/soundArtJS

#sleep 1 min to wait for an internet connection
sleep 1m

#pull any updates
git pull

#RUN THE PROGRAM!!! :D
python3 bathroomNoise.py
