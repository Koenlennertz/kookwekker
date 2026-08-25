def on_button_pressed_a():
    global timerWaarde
    timerWaarde = timerWaarde + 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global startTimer
    startTimer = not (startTimer)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global timerWaarde
    if timerWaarde >= 10:
        timerWaarde = timerWaarde - 10
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global timerWaarde
    timerWaarde = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

startTimer = False
timerWaarde = 0
timerWaarde = 0
startTimer = False

def on_every_interval():
    global timerWaarde
    if startTimer == True:
        if timerWaarde > 0:
            timerWaarde = timerWaarde - 1
        elif timerWaarde < 0:
            timerWaarde = timerWaarde + 1
        else:
            music.play(music.builtin_playable_sound_effect(soundExpression.slide),
                music.PlaybackMode.UNTIL_DONE)
loops.every_interval(1000, on_every_interval)

def on_forever():
    basic.show_string("" + str(Math.idiv(timerWaarde, 60)) + ":" + str(timerWaarde % 60))
basic.forever(on_forever)
