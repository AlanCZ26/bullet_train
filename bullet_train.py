import matplotlib.pyplot as plt
import numpy as np

# Numbers attached at the bottom of the file. Graph from MatPlotLib.


mass_bullet = 0.453592
# 1lb = apprx 0.453592kg, so we set the mass of our bullets to this value.
# 1lb being defined by the problem.

velo_train = 0
# Start at zero velocity (defined in the problem)

mass_ammo = 600
# 600kg of ammo, defined by the problem.

mass_train= 10000 + mass_ammo
# the mass of the train is defined in the problem, and we're adding the mass of the bullets to that since it's not already included.
# We must include the mass of the bullets because we're accelerating them at the same time.

fired = 0
#start having not shot any bullets

velo_prev = velo_train
# in case we want a different initial velocity

printer = []
time_list = []
velo_list = []
accel_list = []
# for printing and matplotlib.

#we will assume no friction as stated in the problem. We will also assume the gun shoots at exactly 60 bullets per second.
while (mass_ammo - mass_bullet > 0): # until we don't have enough ammo for one bullet

    fired += 1 # increment bullets shot
    
    mass_train -= mass_bullet 
    # decrement train mass_trainby how much the bullet is firing to split the two into different objects before the calculation
    
    velo_train += 1010 * mass_bullet / mass_train 
    # momentum remains constant, and since the bullet gains -1010m/s * 0.45kg of momentum, the train must gain the same amount.
    # as a result, the train's velocity must increase by 1010 * [bullet mass] / [train mass].
    # We know the bullet gains -1010 * 0.45kgm/s of momentum since we are assuming the muzzle velocity is exactly 1010m/s, and the bullets are a uniform 1lb.
    # Also, since we only care about delta v (change in velo), the 1010m/s is constant and doesn't change as the train speeds up.

    mass_ammo -= mass_bullet
    # update how much ammo we have left

    accel_cur = (velo_train - velo_prev) / (1/60)
    # acceleration = difference in velocity divided by time.
    # we're assuming exactly 60 bullets per second so time is exactly [fired shots] / 60.

    velo_prev = velo_train
    # since all of our math with updating stuff is done at this point, 

    printer.append("ammo left: " + str(round(mass_ammo, 2)) + "kg, v: " + str(round(velo_train, 5)) + "m/s, Fired: " + str(fired) + " bullets / Time: " + str(round(fired / 60, 5)) + " / accel: " + str(round(accel_cur, 5)))
    # saving our data


    time_list.append(fired/60)
    velo_list.append(velo_train)
    accel_list.append(accel_cur)
    # for matplotlib. time calculated as above.

    

print(printer[0])
print(printer[1])
print(printer[-1])


print("work total: " + str(round(0.5 * mass_train * velo_train ** 2, 4)))
# "From Newton's second law, it can be shown that work on a free (no fields), rigid (no internal degrees of freedom) body, is equal to the change in kinetic energy Ek corresponding to the linear velocity and angular velocity of that body" - wikipedia, https://en.wikipedia.org/wiki/Work_(physics)#Work_and_energy
# Since this is the case for our train, as well as since we have no angular component, our total work is simply equal to total change in kinetic energy.
# Kinetic energy calculated as 1/2 m*v^2.



# Matplotlib formatting borrowed from Ryan

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


"""
ammo left: 599.55kg, v: 0.04322m/s, Fired: 1 bullets / Time: 0.01667 / accel: 2.59329
ammo left: 599.09kg, v: 0.08644m/s, Fired: 2 bullets / Time: 0.03333 / accel: 2.5934
ammo left: 0.35kg, v: 58.8174m/s, Fired: 1322 bullets / Time: 22.03333 / accel: 2.74867
work total: 17298043.2423
"""