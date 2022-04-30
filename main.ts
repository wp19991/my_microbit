input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(control.millis() / 1000)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let a_list = [5, 3, 4, 1]
    a_list.sort()
    a_list.push(2)
    for (let i of a_list) {
        basic.showNumber(i)
    }
    basic.clearScreen()
})
