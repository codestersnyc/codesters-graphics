import codesters
import time

stage = codesters.Environment()
stage.set_background("summer")


sprite = codesters.Sprite("Alien-1")
global sprite
sprite.move_left(200)

sprite3 = codesters.Sprite("")
global sprite3

sprite2 = codesters.Sprite("Alien-2")
sprite2.set_size(0.8)
global sprite2
sprite2.move_right(200)

sprite.physics_on()
#sprite.gravity_off()
sprite.set_drag_on()

sprite2.physics_on()
#sprite2.gravity_off()
sprite2.set_drag_on()

sprite3.physics_on()
#sprite3.gravity_off()
sprite3.set_drag_on()


print codesters.Manager.elements

# IF YOU SWAP SPRITE AND SPRITE2 HERE, WHAT IS PRINTED DOES NOT CHANGE. AT ALL.
sprite.print_corners()
sprite2.print_corners()
sprite3.print_corners()

def collision():
    sprite2.yspeed = -abs(sprite2.yspeed)
    if (sprite2.xspeed < 0):
        sprite2.xspeed -= 0.1
    if (sprite2.xspeed > 0):
        sprite2.xspeed += 0.1
        # add any other actions...

sprite3.event_collision(collision)

def click():
    print "hello"
sprite.event_click(click)

def click2():
    print "hello2"
sprite2.event_click(click2)

def click3():
    print "hello3"
sprite2.event_click(click3)

def key():
    print "key"
sprite.event_key('enter', key)

#sprite3.jump(16)

sprite3.collision_on()
sprite2.collision_on()
sprite.collision_on()


#sprite.jump(10)
#sprite.set_x_speed(-4)

#sprite2.set_x_speed(2)

stage.enable_all_walls()
stage.set_bounce(0.8)


def moveToMouse(event):
    #global sprite
    #global sprite2
    #global sprite3
    print event.x - 250, 250 - event.y


stage.event_click(moveToMouse)
