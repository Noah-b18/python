import matplotlib.pyplot as plt
import numpy as np

g = 9.81   

# Engine specifications
massEngine = 0.0241         # kilograms
massFuel = 0.0122           # kilograms

time, thrustData = np.genfromtxt('Estes_C6.csv', delimiter=',', skip_header=5, unpack=True)
totalImpulstion = np.trapezoid(thrustData, x=time)   # 8.817238 Newtons * sec
thrustMax = max(thrustData) 
print(totalImpulstion)  
print(time[[-1]])

thrustTime = time[-1]    # 1.86 seconds

# Rocket specifications
massStructure = 0.089   #kilograms densite pla : 1240,000 kg / m^3
mass = massStructure + massEngine  # 0.113 kilograms
diameter = 0.034        # meters
front_area = np.pi * (diameter / 2)**2 

dt = 0.01
t = np.arange(-5, 20, dt)
vel = 0.0
alt = 0.0

list_a = []
list_v = []
list_y = []
list_f = []
impact_time = None
was_launched = False

for tps in t:
    if tps >= time[0]:
        was_launched = True
    
    thrust = np.interp(tps, time, thrustData)
    
    consum_massFuel = (thrust * dt) / totalImpulstion * massFuel
    mass -= consum_massFuel
    weight = mass * g 
    D = 0.5 * 1.225 * abs(vel) * vel * front_area * 0.6
    if alt <= 0 :
        resist = weight
    else:
        resist = 0

    f_total = thrust - weight - D + resist

    if tps < 0 or alt <= 0 and tps > time[-1]:
        alt = 0
        vel = 0
        f_total = 0
        if  was_launched and impact_time is None:
            impact_time = tps

    acc = f_total / mass
    vel += acc * dt
    alt += vel * dt

    list_a.append(acc)
    list_v.append(vel)
    list_y.append(alt)
    list_f.append(f_total)


max_alt_idx = list_y.index(max(list_y))
max_alt_t = t[max_alt_idx]

plt.figure(figsize=(10, 6))
# plt.plot(t, list_f, label='Force totale')
# plt.plot(t, list_a, label='Accélération max : {:.2f} m/s²'.format(max(list_a)))
plt.plot(t, list_v, label='Vitesse max : {:.2f} m/s ou {:.2f} km/h' .format(max(list_v), max(list_v) * 3.6))
plt.plot(t, list_y)
plt.plot(max_alt_t, max(list_y), 'go')
plt.annotate('Altitude max : {:.2f} m'.format(max(list_y)), (max_alt_t, max(list_y)),
             textcoords='offset points', xytext=(10, 0), ha='left', va='center', fontsize=9)
plt.axvline(x=thrustTime, color='red', linestyle='--', linewidth=0.5)
if impact_time is not None:
    plt.scatter(impact_time, 0, color = 'orange', label = 'Impact :  {:.2f} s'.format(impact_time))
plt.legend(loc='lower left')
plt.grid()
plt.show()