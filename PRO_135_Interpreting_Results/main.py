import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Gravity_Dist_Support.csv')
df_list = df.values.tolist()

name = []
dist = []
mass = []
radius = []
gravity = []

for i in df_list:
    name.append(str(i[0]))
    dist.append(float(i[1]))
    mass.append(float(i[2]))
    radius.append(float(i[3]))
    gravity.append(float(i[4]))

plt.figure(figsize=(10,5))
plt.bar(x = name, height = mass)
plt.title("Name VS Mass")
plt.xlabel("Name", fontweight='bold', fontsize=12)
plt.ylabel("Mass", fontweight='bold', fontsize=12)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10,5))
plt.bar(x = name, height = radius)
plt.title("Name VS Radius")
plt.xlabel("Name", fontweight='bold', fontsize=12)
plt.ylabel("Radius", fontweight='bold', fontsize=12)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10,5))
plt.bar(x = name, height = dist)
plt.title("Name VS Distance")
plt.xlabel("Name", fontweight='bold', fontsize=12)
plt.ylabel("Distance(Light Years)", fontweight='bold', fontsize=12)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10,5))
plt.bar(x = name, height = gravity)
plt.title("Name VS Gravity")
plt.xlabel("Name", fontweight='bold', fontsize=12)
plt.ylabel("Gravity", fontweight='bold', fontsize=12)
plt.xticks(rotation=90)
plt.show()

# INSIGHTS

# Speaking of the first Graph(Name vs Mass), we can conclude that more than half of the exoplanets are very light-weight as compared to the Sun. Exoplanet named "Sirius" weighs more than double than that of Sun
# Speaking of the second Graph(Name vs Radius), we see that almost half the exoplanets have very small radius. "Altair" and "Fomalhaut" have biggest radius in this categorization
# Speaking of the third Graph(Name vs Distance), we see that all the exoplanets are very far from us, "Alpha Centauri" being the clossest
# Speaking of the forth Graph(Name vs Gravity), we can conclude that the lowest value of gravity is somewhere about 150 and the highest around 330