def on_button_pressed_a():
    basic.show_number(count)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global count
    basic.show_number(0)
    count = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global count
    count += 1
    basic.show_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
basic.show_number(0)
count = 0