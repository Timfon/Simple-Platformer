from pyray import *

class Player:
    def __init__ (self):
        self.player = Rectangle(400, 200, 20, 20)

        self.x_momentum = 0
        self.y_momentum = 0
        self.jumped = False

        self.controlled_jump = 0
        self.dy = 0
        self.dx = 0
    #class methods have self.
    def move(self):
        self.y_momentum += 1
        if self.y_momentum > 10:
            self.y_momentum = 10
        self.dy += self.y_momentum

        if is_key_down(KEY_D):
            self.dx += 1
        elif is_key_down(KEY_A):
            self.dx -= 1
        if is_key_down(KEY_R):
            self.player.x = 400
            self.player.y = 200
        
        if is_key_down(KEY_SPACE) and not self.jumped:
            self.controlled_jump += 1
            if 1 <= self.controlled_jump <= 5:
                self.y_momentum = -8
            elif 5 <= self.controlled_jump <= 10:
                self.y_momentum = -8
            elif self.controlled_jump >= 10:
                self.y_momentum = -8
                self.jumped = True
                self.controlled_jump = 0
        elif is_key_up(KEY_SPACE):
            self.jumped = True

    def update_pos(self):
        self.player.x += self.dx
        self.player.y += self.y_momentum
        self.dx = self.dx * 0.90
        draw_rectangle_rec(self.player, MAGENTA)

        
