import numpy as np

def f(x, defence, pierce):
    E = 0
    if defence > pierce:
        E = defence - pierce

    return x * (1 - E/(E + 596.70))  # 596.7 is computed from regression


n_defence = 100
n_pierce = 50
v_defence = np.linspace(10, 1000, n_defence)
v_pierce = np.linspace(10, 500, n_pierce)

defence_val, pierce_val = np.meshgrid(v_defence, v_pierce)

damage_val = np.array(defence_val, copy=True)

for i in range(n_defence):
    for j in range(n_pierce):
        damage_val[j][i] = f(100, defence_val[j][i], pierce_val[j][i])



import matplotlib.pyplot as plt
from matplotlib import cm

from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization!
fig = plt.figure()
ax = Axes3D(fig)
ax.set_zlim3d(0, 100)
ax.set_zlabel("Damage level %")
ax.set_xlabel("Defence")
ax.set_ylabel("Pierce")

surf = ax.plot_surface(defence_val, pierce_val, damage_val,  cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
