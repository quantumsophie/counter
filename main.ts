input.onButtonPressed(Button.A, function () {
    basic.showNumber(count)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(count)
    count += 5
})
input.onButtonPressed(Button.B, function () {
    count += 2
    basic.showNumber(count)
})
let count = 0
basic.showNumber(0)
count = 0
