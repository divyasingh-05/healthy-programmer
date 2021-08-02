from pygame import mixer
from datetime import datetime
from time import time
def musiconloop (file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        input_from_user=input()
        if input_from_user==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
watersecs=1800
eyesecs=3000
exercisesecs=4200
while True:
    if time()-init_water>watersecs:
        print("Water drinking time. Enter 'Drank' to stop music")
        musiconloop("water song.mp3","Drank")
        init_water = time()
        log_now("Water drink at ")
    if time()-init_eyes>eyesecs:
        print("Eyes exercise time. Enter 'Done' to stop music")
        musiconloop("eyes song.mp3","Done")
        init_eyes = time()
        log_now("Eyes exercise done at ")
    if time()-init_exercise>exercisesecs:
        print("Physical exercise time. Enter 'Done' to stop music")
        musiconloop("exercise song.mp3","Done")
        init_exercise = time()
        log_now("Physical exercise done at ")