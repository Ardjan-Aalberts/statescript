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


def meta_data():
    f = open('logs.txt', 'a')
    f.write('This terminal keeps records off your activities.' + '\n'
            + 'Made by S0lid' + '\n'
            + 'By using this software you agree to buy the owner of this application at least five beer.' + '\n'
            + '+------------------------------------------------------------------------------+' + '\n')
    f.close()

meta_data()


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
