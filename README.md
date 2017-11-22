# Sound art project

The webpage is contained within the folder public_html this is the webpage root folder. The files `ART.txt`, `jquery.min.js`, `SculptureSound.m4a`, and `SculptureSound.wav` are not used currently in the project.

`ScultpureSound.wav` and `SculptureSound.m4a` are different versions of the original sound file that was recorded, we now however have split up the file and cut out some undesired bits and we end with 31 separate sounds, each of these is included in the `Sound` folder.

The actual webpage (`index.html`) simply goes along in a loop (more or less) and plays a random audio file from the 31 files in the `Sound` folder. The program also has knowledge of how long each sound file is, and will play files faster or slower (up to x4 speed and as low as x.25 speed) so as to try and reach some target length of time for the file to play. This times at which a sound is played and the length it plays for is preprogrammed in based on the location of each of the wood bars put on the sculpture.