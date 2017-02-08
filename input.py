import datetime
import sched
import time
from pygame import mixer


s = sched.scheduler(time.time, time.sleep)


def play_sound():
    mixer.init()
    mixer.music.load('msg.mp3')
    mixer.music.play()

play_sound()


def write_file(now, activity):
    f = open('logs.txt', 'a')
    f.write('Time: ' + now + ', Activity: ' + activity + '\n')
    f.close()


def user_activity(sc):
    play_sound()
    now = str(datetime.datetime.now())
    activity = raw_input('What the fuck are u doing?')
    print now, activity
    s.enter(1800, 1, user_activity, (sc,))
    write_file(now, activity)

s.enter(0, 1, user_activity, (s,))
s.run()
