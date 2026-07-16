import matplotlib.pyplot as plt
import numpy as np

g = 9.81   

# Engine specifications
massEngine = 0.0241         # kilograms
massFuel = 0.0122           # kilograms

totalImpulstion = 9.576     # Newtons * sec
thrustMax = 15.3            # Newtons
thrustCrusing = 4.5         # Newtons

thrustTime_max = 0.22       # seconds
thrustTime_crusing = 1.38   # seconds
thrustTime = thrustTime_max + thrustTime_crusing    # 1.6 seconds

# Rocket specifications
massStructure = 0.089   #kilograms densite pla : 1240,000 kg / m^3
mass = massStructure + massEngine  # kilograms
diameter = 0.034        # meters
front_area = 0.000962   # square meters
print(mass)



dt = 0.01
t = np.arange(-5, 20, dt)
vel = 0.0
alt = 0.0

list_a = []
list_v = []
list_y = []
impact_time = None
was_launched = False

for tps in t:

    if tps >= 0 and tps <= thrustTime_max:
        thrust = thrustMax
        was_launched = True
    elif tps >= thrustTime_max and tps <= thrustTime:
        thrust = thrustCrusing
    else:
        thrust = 0
    
    consum_massFuel = (thrust * dt) / totalImpulstion * massFuel
    mass -= consum_massFuel
    weight = mass * g 
    D = 0.5 * 1.225 * abs(vel) * vel * front_area * 0.8
    f_total = thrust - weight - D

    if tps < 0 or alt <= 0 and tps > 0.5:
        alt = 0
        vel = 0
        f_total = 0
        if impact_time is None and was_launched:
            impact_time = tps

    acc = f_total / mass
    vel += acc * dt
    alt += vel * dt

    list_a.append(acc)
    list_v.append(vel)
    list_y.append(alt)


max_alt_idx = list_y.index(max(list_y))
max_alt_t = t[max_alt_idx]

plt.figure(figsize=(10, 6))
plt.plot(t, list_y)
plt.plot(t, list_v, label='Vitesse max : {:.2f} m/s ou {:.2f} km/h' .format(max(list_v), max(list_v) * 3.6))
plt.plot(max_alt_t, max(list_y), 'go')
plt.annotate('Altitude max : {:.2f} m'.format(max(list_y)), (max_alt_t, max(list_y)),
             textcoords='offset points', xytext=(10, 0), ha='left', va='center', fontsize=9)
plt.axvline(x=thrustTime, color='red', linestyle='--', linewidth=0.5)
plt.scatter(impact_time, 0, color = 'orange', label = 'Impact :  {:.2f} s'.format(impact_time))
plt.legend(loc='lower left')
plt.grid()
plt.show()

