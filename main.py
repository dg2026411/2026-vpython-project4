body = box(pos=vec(0,0,0), size=vec(1,2,0.5), color=color.white)
head = box(pos=vec(0,1.5,0), size=vec(0.8,0.8,0.5), color=color.white)
left_arm = box(pos=vec(-0.8,0.5,0), size=vec(0.4,1,0.3), color=color.white)
right_arm = box(pos=vec(0.8,0.5,0), size=vec(0.4,1,0.3), color=color.white)
left_leg = box(pos=vec(-0.4,-1.5,0), size=vec(0.4,1,0.3), color=color.white)
right_leg = box(pos=vec(0.4,-1.5,0), size=vec(0.4,1,0.3), color=color.white)
left_eye = box(pos=vec(-0.2,1.7,0.3), size=vec(0.2,0.2,0.1), color=color.black)
right_eye = box(pos=vec(0.2,1.7,0.3), size=vec(0.2,0.2,0.1), color=color.black)
mouth = box(pos=vec(0,1.3,0.3), size=vec(0.4,0.1,0.1), color=color.black)
Human=compound([body,head,left_arm,right_arm,left_leg,right_leg,left_eye,right_eye,mouth])
Human =(pos = vec(0,-4,1.5))
at=sphere(pos=vec (5.5,4,0),radius=1)
that=sphere(pos=vec (4,4,0),radius=1)
all=sphere(pos=vec (5,5,0),radius=1)
of=sphere(pos=vec (6,5,0),radius=1)
it=sphere(pos=vec (7,4,0),radius=1)
cloud=compound([at,that,all,of,it])
sphere(pos=vec (-6,4,0),radius=1)
sphere(pos=vec (-7,4,0),radius=1)
sphere(pos=vec (-6.5,5,0),radius=1)
sphere(pos=vec (-7.5,5,0),radius=1)
sphere(pos=vec (-8,4,0),radius=1)
box(pos=vec(0,-5,0),size = vec(30,1,5))
rock=ellipsoid(pos=vec(-4, 2, 1.5), length=1.2, height=0.9, width=0.5)
import random
l = label(pos=vec(14,9,0))
g = vec(0,-9.8,0)
rock.v=vec(0,0,0)
while True :
    l.text = clock()
    rate(100)
    k = keysdown()
    if 'left' in k :
        b.pos.x = b.pos.x - 0.1
    if 'right' in k :
        b.pos.x = b.pos.x + 0.1

    dt=0.01
    if rock.pos.y>=-5:
        rate(100)
        rock.pos=rock.pos +rock.v*dt
        rock.v= rock.v + g*dt
        cloud.pos.x = cloud.pos.x + random.uniform(-1,1)
    if rock.pos.y <= -5 : 
        rock.pos = vec(random.randint(-15,15), 2,1.5)
        g = vec(0,-9.8,0)
        rock.v=vec(0,0,0)
