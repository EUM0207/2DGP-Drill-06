from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

CHARA_W = 802 // 8
CHARA_H = 402 // 4

hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
dir = 1
is_running = False


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #elif event.type == SDL_MOUSEMOTION:
        #    x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    #update_canvas()
    #frame = (frame + 1) % 8

    hand.draw(hand_x, hand_y)

    dx = hand_x - x
    dy = hand_y - y
    distance = (dx**2 + dy**2) ** 0.5

    if distance < 8:
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
        is_running = False
    else:
        x += dx / distance * 8
        y += dy / distance * 8

        if dx > 0:
            dir = 1
        else:
            dir = -1

        is_running = True

    if is_running:
        if dir == 1:
            y_index = 1
        else:
            y_index = 0
    else:
        if dir == 1:
            y_index = 3
        else:
            y_index = 2

    character.clip_draw(frame * CHARA_W, y_index * CHARA_H, CHARA_W, CHARA_H, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.05)

close_canvas()




