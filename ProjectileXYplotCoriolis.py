import matplotlib.pyplot as plt

X = []
Y = []

inFile = open("projectileCoriolisData.txt", "r")
for line in inFile:
    t, x, y, z, v_x, v_y, v_z, a_x, a_y, a_z = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
inFile.close()

plt.xlabel("$x$ (m)")
plt.ylabel("$y$ (m)")
plt.plot(X,Y)
plt.show()