from pyray import *
from raylib import *
from random import choice,randint
init_window(1280,720,'h')
pos=Vector2(1280/2,720/2)
dir=Vector2()
speed=300

circles=[(
    Vector2(randint(-2000,2000),randint(-1200,1200)),
    randint(30,150),
    choice([RED,BLUE,PINK,YELLOW])
    )
    for i in range(100)
]
camera=Camera2D()
camera.target=pos
camera.zoom=1
camera.offset=pos
camera.rotation=0

while not window_should_close():
    dt=get_frame_time()
    camera.target=pos
    zoom=int(is_key_down(KEY_Q))-int(is_key_down(KEY_E))
    camera.zoom+=zoom*dt*1
    rotate= int(is_key_down(KEY_LEFT))-int(is_key_down(KEY_RIGHT))
    camera.rotation+=rotate*dt*100
    dir.x=int(is_key_down(KEY_D))-int(is_key_down(KEY_A))
    dir.y=int(is_key_down(KEY_S))-int(is_key_down(KEY_W))
    pos.x+=dt*speed*dir.x
    pos.y+=dt*speed*dir.y
    begin_drawing()
    begin_mode_2d(camera)
    ClearBackground(BLACK)
    for circle in circles:
        draw_circle_v(*circle)
    draw_circle_v(pos,30,GREEN)
    end_mode_2d()
    end_drawing()
CloseWindow()