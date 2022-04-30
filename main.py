
def on_button_pressed_a():
    basic.show_number(control.millis()/1000)

def on_button_pressed_b():
    a_list = [5,3,4,1]
    a_list.sort()
    a_list.push(2)
    for i in a_list:
        basic.show_number(i)
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)