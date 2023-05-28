from levels import *
from pyray import *
from Player import *

def main():
    #level number
    screen_width: int = 800
    screen_height: int = 400

    init_window(screen_width, screen_height, "Platformer")
    set_target_fps(60)
    player = Player()
    levels = Level()

    while not window_should_close():
        begin_drawing()

        tile_rects = levels.initialize_levels()

        player.move()

        for tile in tile_rects:
            draw_rectangle_rec(tile, GRAY)

            if check_collision_recs((player.player.x + player.dx, player.player.y, player.player.width, player.player.height), tile):
                player.dx = 0

            if check_collision_recs((player.player.x, player.player.y + player.y_momentum, player.player.width, player.player.height), tile):
                print(player.y_momentum)
                if player.y_momentum < 0:
                    player.y_momentum = (tile.y + 20) - player.player.y
                    player.y_momentum = 0
                elif player.y_momentum >= 0:
                    player.y_momentum = tile.y - (player.player.y + 20)
                    player.y_momentum = 0
                player.jumped = False
                player.controlled_jump = 0




        #refactor levelswitch
        '''if player.x > 800:
            n += 1
            player.x = 0'''

        draw_fps(400, 200)
        clear_background(RAYWHITE)
        end_drawing()


if __name__ == "__main__":
    main()

close_window()
