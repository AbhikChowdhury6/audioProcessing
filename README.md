# audioProcessing
using dep test envioronment
to set up depTest enviromnment
I cloned the CrisperWhsper repo
then i checked out the devlop branch git checkout develop
the I pip install -r requirements.txt

to capture test recording on linux
arecord test15.mp3 --duration=15


process for audio transfers

- do all the recordings I want
- go into icloud on my iphone, compress the just press record file
- go to icloud on my desktop and download the file to a recent audio captures folder
- delete the just press record folder

Recording process 

- do it from the iphone and with for the bigger battery
- honestly most of the time I’m alone and can just leave the recording running
- I turn it off for
    - talking to my dad
    - picking up a call
    - being in public
    - leaving the car
- I’ll just reach into the phone in my pocket to stop the recording whenever that happens, I really don’t talk to other people often
- TODO: test to see if the airpods to phone connection is more reliable for recording

for the intake code

- unzip the folder
- go through every file
- read it in
- generate crisper whisper transcriptions - save using segment format
- make 10 minute segments
- save the 10 minute segments to the right

I want the data structure to

- down sample to 16khz
- be in segments that are 10 minutes max
- store audio in well compressed codec
- named with the start and end time to the second
- round the end to the next full second
- each day will have it’s own folder
- then each month will have it’s own folder

