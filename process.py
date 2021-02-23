import pickle
import os
with open('data', 'rb') as f:
    a = pickle.load(f)

for i, m in a.items():

    folder = 'Season_%d'%i
    os.system('mkdir '+folder)
    for name, content in m.items():
        with open('%s/%s.md'%(folder, name), 'w') as f:
            f.write('# %s\n'%name)
            f.write(content)
