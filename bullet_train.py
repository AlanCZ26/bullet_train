import matplotlib.pyplot as plt
import numpy as np

# Results attached at the bottom of the file. Graph from MatPlotLib, MatPlotLib formatting by Ryan Pan.

# ================================
#        INITIAL CONDITIONS
# ================================

mass_bullet = 0.453592 # kg
# 1lb = apprx 0.453592kg, so we set the mass of our bullets to this value.
# 1lb being defined by the problem.

velo_train = 0 # m/s
# Start at zero velocity (defined in the problem)

mass_ammo = 600 # kg
# 600kg of ammo, defined by the problem.

mass_train= 10000 + mass_ammo # kg
# the mass of the train is defined in the problem, and we're adding the mass of the bullets to that since it's not already included.
# We must include the mass of the bullets because we're accelerating them at the same time as the train.

shots_per_second = 60 # shots per second
# Defined in the problem, exactly 60 bullets per second

muzzle_velocity = 1010 #m/s
# defined in the problem

mu = 0
# no friction in default conditions

accel_g = 9.81 # m/s^2
# gravity constant


# ================================
#           OTHER SETUP
# ================================

fired = 0
#start having not shot any bullets

velo_prev = velo_train
# in case we want a different initial velocity

printer = []
time_list = []
velo_list = []
accel_list = []
# for printing and matplotlib.

# ================================
#            MAIN LOOP
# ================================

# We will assume no friction as stated in the problem. This means our final velocity is higher than reality. Net work would decrease, since friction would be negative work (force in the opposite direction).
# We will assume that this is a closed system, and any momentum imparted in the bullets exactly equals the momentum imparted into the train, with zero loss.

while (mass_ammo - mass_bullet >= 0): # until we don't have enough ammo for one bullet

    fired += 1 # increment bullets shot
    
    mass_train -= mass_bullet 
    # decrement train mass_trainby how much the bullet is firing to split the two into different objects before the calculation
    
    velo_train += muzzle_velocity * mass_bullet / mass_train 
    # momentum remains constant, and since the bullet gains -1010m/s * 0.45kg of momentum, the train must gain the same amount.
    # as a result, the train's velocity must increase by 1010 * [bullet mass] / [train mass]. {since 1010m/s * [bullet mass]kg = [delta v (train)]m/s * [train mass]kg}
    # We know the bullet gains -1010 * 0.45kgm/s of momentum since we are assuming the muzzle velocity is exactly 1010m/s, and the bullets are a uniform 1lb.
    # Also, since we only care about delta v (change in velo), the 1010m/s is constant and doesn't change as the train speeds up.

    mass_ammo -= mass_bullet
    # update how much ammo we have left

    accel_cur = (velo_train - velo_prev) / (1/shots_per_second)
    # acceleration = change in velocity divided by change in time.
    # we're assuming exactly 60 bullets per second so time is exactly bullets / bullets/second
    # we use this number for the matplotlib visualization

    force_fric = mass_train * accel_g * mu
    velo_train = max(0, velo_train - (force_fric / mass_train) * (1/shots_per_second))
    # calculate friction (Ffr <= mu Fn, we make sure it can't go negative)
    # i put this here to look at effects of assumtions (not used for normal conditions)

    velo_prev = velo_train
    # since all of our math with updating stuff is done at this point, we can save our previous velocity to be used in the next iteration

    printer.append("velocity: " + str(round(velo_train, 5)) + "m/s // Fired: " + str(fired) + " bullets // Time: " + str(round(fired / shots_per_second, 5)) + " // accel: " + str(round(accel_cur, 5)))
    # saving our data in string format


    time_list.append(fired/shots_per_second)
    velo_list.append(velo_train)
    accel_list.append(accel_cur)
    # for matplotlib. time calculated as above.


# ================================
#       DATA VISUALIZATION
# ================================    

print(printer[0]) # first shot
print(printer[1]) # second shot
print(printer[-1]) # last shot


print("work total: " + str(round(0.5 * mass_train * velo_train ** 2, 4)) + " joules")
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


# ================================
#            RESULTS
# ================================

# default conditions:
"""
velocity: 0.04322m/s // Fired: 1 bullets // Time: 0.01667 // accel: 2.59329
velocity: 0.08644m/s // Fired: 2 bullets // Time: 0.03333 // accel: 2.5934     
velocity: 58.8174m/s // Fired: 1322 bullets // Time: 22.03333 // accel: 2.74867
work total: 17298043.2423 joules
"""

# if the bullet was 1kg instead of 1lb:
"""
velocity: 0.09529m/s // Fired: 1 bullets // Time: 0.01667 // accel: 5.71752
velocity: 0.19059m/s // Fired: 2 bullets // Time: 0.03333 // accel: 5.71806
velocity: 58.85446m/s // Fired: 600 bullets // Time: 10.0 // accel: 6.06   
work total: 17319234.8307 joules
"""

# if we had 6000kg of ammo (10x):
"""
velocity: 0.02863m/s // Fired: 1 bullets // Time: 0.01667 // accel: 1.71803
velocity: 0.05727m/s // Fired: 2 bullets // Time: 0.03333 // accel: 1.71808     
velocity: 474.67806m/s // Fired: 13227 bullets // Time: 220.45 // accel: 2.74867
work total: 1126634428.4607 joules
"""

# if muzzle velocity was 2020m/s (2x):
"""
velocity: 0.08644m/s // Fired: 1 bullets // Time: 0.01667 // accel: 5.18658
velocity: 0.17289m/s // Fired: 2 bullets // Time: 0.03333 // accel: 5.1868
velocity: 117.63481m/s // Fired: 1322 bullets // Time: 22.03333 // accel: 5.49734
work total: 69192172.9693 joules
"""

# if mu was 0.1 instead of 0:
"""
velocity: 0.02687m/s // Fired: 1 bullets // Time: 0.01667 // accel: 2.59329
velocity: 0.05374m/s // Fired: 2 bullets // Time: 0.03333 // accel: 2.5934     
velocity: 37.2027m/s // Fired: 1322 bullets // Time: 22.03333 // accel: 2.74867
work total: 6920449.3278 joules
"""