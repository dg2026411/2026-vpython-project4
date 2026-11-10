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
b=box(texture = "https://i.postimg.cc/gJyzG0cv/geulim1.png",pos=vec(0,-4,0))
box(pos=vec(0,-5,0),size = vec(30,1,5))

import random
l = label(pos=vec(14,9,0))
while True :
    rate(100)
    l.text = clock()
    k = keysdown()
    if 'left' in k :
        b.pos.x = b.pos.x - 0.1
    if 'right' in k :
        b.pos.x = b.pos.x + 0.1
    g = vec(0,-9.8,0)
    rock.v=vec(0,0,0)
    dt=0.01
    while rock.pos.y>=-5:
        rock.pos=rock.pos +rock.v*dt
        rock.v= rock.v + g*dt
    if rock.pos.y <= -5 : 
        rock.pos = vec(random.randint(-15,15), 2,1.5)

