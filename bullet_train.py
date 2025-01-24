import matplotlib.pyplot as plt
import numpy as np





#1322 bullets

total_ammo = 600
mass_bullet = 0.453592
v_train = 0
mass = 10000 + total_ammo
time = 0
fired = 0
x = []
y = []
v_p = v_train

while (total_ammo - mass_bullet > 0):
    fired += 1
    mass -= mass_bullet
    v_train += 1010 * mass_bullet / mass
    total_ammo -= mass_bullet
    print("ammo left: " + str(total_ammo) + ", v: " + str(v_train) + " / Fired bullets: " + str(fired) + " / Time taken: " + str(fired / 60) + " / accel: " + str((v_train - v_p) / (1/60)))
    y.append(v_train)  
    x.append(fired / 60)
    v_p = v_train


# make the data


# size and color:
sizes = 30
colors = [30] * fired

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, sizes, colors, vmin=0, vmax=100)


plt.show()