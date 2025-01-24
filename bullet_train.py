import matplotlib.pyplot as plt
import numpy as np





#1322 bullets

mass_ammo = 600
mass_bullet = 0.453592
velo_train = 0
mass_train= 10000 + mass_ammo

fired = 0

velo_prev = velo_train

printer = []

time_list = []
velo_list = []
accel_list = []

sum_work = 0


while (mass_ammo - mass_bullet > 0):
    fired += 1 # increment bullets shot
    mass_train-= mass_bullet # decrement train mass_trainby how much the bullet is firing to split the two into different objects before the calculation
    velo_train += 1010 * mass_bullet / mass_train
    mass_ammo -= mass_bullet
    accel_cur= (velo_train - velo_prev) / (1/60)
    velo_prev = velo_train

    force_cur = mass_train * accel_cur
    sum_work += force_cur * velo_train * 1/60
    
    printer.append("ammo left: " + str(round(mass_ammo, 2)) + "kg, v: " + str(round(velo_train, 5)) + "m/s, Fired: " + str(fired) + " bullets / Time: " + str(round(fired / 60, 5)) + " / accel: " + str(round(accel_cur, 5)))
    
    time_list.append(fired/60)
    velo_list.append(velo_train)
    accel_list.append(accel_cur)

    

print(printer[0])
print(printer[1])
print(printer[-1])
print(sum_work)


#formatting borrowed from Ryan

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time_list, velo_list, label="Velocity vs Time", color="blue", linewidth=2)
plt.title("Time vs Velocity", fontsize=16)
plt.xlabel("Time (seconds)", fontsize=14)
plt.ylabel("Velocity (m/s)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)

plt.subplot(2, 1, 2)
plt.plot(time_list, accel_list, label="Acceleration vs Time", color="red", linewidth=2)
plt.title("Time vs Acceleration", fontsize=16)
plt.xlabel("Time (seconds)", fontsize=14)
plt.ylabel("Acceleration (m/s²)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()