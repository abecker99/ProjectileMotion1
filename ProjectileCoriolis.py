import math

g = 9.8 #in m/s^2
w = 0.0000727 #earth rotational speed rad/s


def acceleration(v_x, v_y, v_z, C, m):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y)/m - 2*v_z*w_y
    #coriolisi 2*-vz*w_y
    #j 2*vz*w_x
    #k 2*(v_x*w_y - v_y*w_x)
    a_y = -g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y)/m + 2*v_z*w_x
    a_z = 2*(v_x*w_y - v_y*w_x)
    return a_x, a_y, a_z # computes acceleration w/ gravity and drag force

def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    z = z + v_z*dt + 0.5*a_z*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    v_z = v_z*dt + a_z*dt
    return x, y, z, v_x, v_y, v_z #updates position & velocity

v_0 = float(input("What is the magnitude of the initial velocity?: ")) #in m/s
l = float(input("What is the latitude of your location?: ")) #in degrees
dt = float(input("What is the size of the time step?: "))
m = float(input("What is the projectile mass?: ")) # 0.04593 in kg
C = float(input("What is the drag coefficient?: ")) # 4*10^-4 #in kg/m
theta = 90 - l

w_x = -w*math.cos(theta*math.pi/180.0)
w_y = w*math.sin(theta*math.pi/180.0)
v_x = v_0*math.cos(theta*math.pi/180.0)
v_y = v_0*math.sin(theta*math.pi/180.0)
v_z = v_0

outFile = open("projectileCoriolisData.txt", "w")

t = 0.0
y = 0.0 #in m
x = 0.0 #in m
z = 0.0
y_max = 0.0
inFlight = True

while (inFlight):
    a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m)
    x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt) 
    t += dt
    if (y >= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(v_x) + " " + str(v_y) + " " + str(v_z) + " " + str(a_x) + " " + str(a_y) + " " + str(a_z) +"\n")
        if (y > y_max):
            y_max = y
    else:
        inFlight = False

outFile.close()

print("Maximum height:", y_max)
print("Horizontal range:", x)