import maestro
import math
import time


# 0 = spinning plate
# 1 = arm
# 2 = arm
# 3 = pen


v = maestro.Controller("/dev/ttyACM0")
# controlor.create_gui(1, 1, "servo", )


v.setRange(0, 6000 - 200, 6000 + 200)
v.setRange(4, 3000, 9000)
v.setRange(5, 3000, 9000)
v.setRange(3, 3000, 9000)

# v.setTarget(0, 6000)
# v.setTarget(4, 6000)
# v.setTarget(5, 6000)
# v.setTarget(3, 6000)


def run(up):
    v.setTarget(3, 3000)
    v.setTarget(0, 6000-15)
    time.sleep(0.5)
    v.setTarget(4, 9000)
    v.setTarget(5, 3000)

    if up:
        v.setTarget(1, 9000)
        v.setTarget(2, 3000)

    else:

        if 0:
            mag = 2000
            offset = -500
            t = 0.0
            dt = 0.025

            x = input()

            A = mag * (math.sin(t) + math.cos(t)) / 2
            B = mag * (math.cos(t) - math.sin(t)) / 2
            pos1 = int(6000 + B + offset)
            pos2 = int(6000 + A + offset)
            v.setTarget(4, pos1)
            v.setTarget(5, pos2)

            time.sleep(1.0)

            v.setTarget(3, 6000)

            time.sleep(0.2)

            v.setTarget(0, 6000 +15)#- 85)

            while True:
                t += dt
                if t > 2*math.pi:
                    t = 0
                A = mag * (math.sin(t) + math.cos(t)) / 2
                B = mag * (math.cos(t) - math.sin(t)) / 2
                pos1 = int(6000 + A + offset)
                pos2 = int(6000 + B + offset)
                v.setTarget(4, pos1)
                v.setTarget(5, pos2)
                time.sleep(0.01)

        if 1:
            mag = 1500
            offset = 200
            t = 0.0

            x = input()

            pos1 = int(6000 + mag * t + offset)
            pos2 = int(6000 - mag * t - offset)
            v.setTarget(4, pos1)
            v.setTarget(5, pos2)

            time.sleep(1.0)

            v.setTarget(3, 6000)

            time.sleep(0.2)

            v.setTarget(0, 6000 + 35)
            dt = 0.01
            while True:
                t += dt
                if (t > 1.0) or (t < -1.0):
                    dt = -dt

                pos1 = int(6000 + mag * t + offset)
                pos2 = int(6000 - mag * t - offset)
                v.setTarget(4, pos1)
                v.setTarget(5, pos2)
                time.sleep(0.01)



run(0)
