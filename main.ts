input.onButtonPressed(Button.A, function () {
    if (timerWaarde >= 10) {
        timerWaarde = timerWaarde - 10
    }
})
input.onGesture(Gesture.LogoUp, function () {
    timerWaarde = 0
    startTimer = false
})
input.onButtonPressed(Button.AB, function () {
    startTimer = !(startTimer)
})
input.onButtonPressed(Button.B, function () {
    timerWaarde = timerWaarde + 10
})
input.onGesture(Gesture.Shake, function () {
    timerWaarde = 0
    startTimer = false
})
let startTimer = false
let timerWaarde = 0
timerWaarde = 0
startTimer = false
loops.everyInterval(1000, function () {
    if (startTimer == true) {
        if (timerWaarde > 0) {
            timerWaarde = timerWaarde - 1
        } else {
            music.play(music.builtinPlayableSoundEffect(soundExpression.slide), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    basic.showString("" + Math.idiv(timerWaarde, 60) + ":" + timerWaarde % 60)
})
