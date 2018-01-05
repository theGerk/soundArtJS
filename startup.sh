#!/bin/sh

#sleep 1 min to wait for an internet connection
sleep 1m

#pull any updates
git pull

#RUN THE PROGRAM!!! :D
python3 /home/pi/soundArtJS/bathroomNoise.py
