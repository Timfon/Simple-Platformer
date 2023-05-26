from pyray import *
init_window(800, 450, "window")

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()