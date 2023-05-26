from levels import *
from pyray import *
screen_width: int = 800
screen_height: int = 400

init_window(screen_width, screen_height, "Platformer")
set_target_fps(60)
player = Rectangle(400, 200, 20, 20)

def main():
    #level number

    
    x_momentum = 0
    y_momentum = 0
    jumped = False

    controlled_jump = 0
    dy = 0
    dx = 0
    while not window_should_close():
        begin_drawing()

        y_momentum += 1
        if y_momentum > 10:
            y_momentum = 10
        dy += y_momentum

        if is_key_down(KEY_D):
            dx += 1
        elif is_key_down(KEY_A):
            dx -= 1
        if is_key_down(KEY_R):
            player.x = 400
            player.y = 200
        
        if is_key_down(KEY_SPACE) and not jumped:
            controlled_jump += 1
            if 1 <= controlled_jump <= 5:
                y_momentum = -8
            elif 5 <= controlled_jump <= 10:
                y_momentum = -8
            elif controlled_jump >= 10:
                y_momentum = -8
                jumped = True
                controlled_jump = 0
        elif is_key_up(KEY_SPACE):
            jumped = True

        for tile in tile_rects:
            draw_rectangle_rec(tile, GRAY)

            if check_collision_recs((player.x + dx, player.y, player.width, player.height), tile):
                dx = 0
            if check_collision_recs((player.x, player.y + y_momentum, player.width, player.height), tile):
                if y_momentum < 0:
                    y_momentum = (tile.y + 20) - player.y
                    y_momentum = 0
                elif y_momentum >= 0:
                    y_momentum = tile.y - (player.y + 20)
                    y_momentum = 0
                jumped = False
                controlled_jump = 0


        player.x += dx
        player.y += y_momentum
        dx = dx * 0.90

        #refactor levelswitch
        if player.x > 800:
            n += 1
            player.x = 0

        draw_rectangle_rec(player, MAGENTA)

        draw_fps(400, 200)
        clear_background(RAYWHITE)
        end_drawing()


if __name__ == "__main__":
    main()

close_window()
