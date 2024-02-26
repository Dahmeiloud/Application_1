import pydub
from pydub import AudioSegment
from pydub.playback import play 
import datetime 

time = input('Entre the alarm : ')
alarm = AudioSegment.from_mp3('sounds/alarm.mp3')
play(alarm)

while True:
    time = datetime.datatime.now()
    now = timo.strftime("%H:%M:%S")
    if now == time:
        medcine = AudioSegment.from_mp3('sounds/Tenbih.mp3')
        play(medcine)
    if now > time:
        break