
"""summant = 20
vec = [0,1,1,4,4]
ind = 3
frac = vec[ind]/summant
rew = 0
rew = (1 - frac)*vec[ind]
print(1-frac)
print("reward: ", rew)
vec[ind] += rew
ind2 = 4


frac2 = vec[ind2]/summant
print(frac2)
print(vec[ind2])
pun = frac2 * vec[ind2]
print("Punishment: ", pun)
print(vec[ind2] - pun)
vec[ind2] -= pun
print(vec)"""
import pandas as pd

df = pd.read_csv('Project Database.csv')
df = df.values.tolist()
print(df)