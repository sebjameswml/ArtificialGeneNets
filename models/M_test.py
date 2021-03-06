import h5py
import numpy as np
from tools import *
import os

# Parameters
dir = 'test' # This folder should exist! It should contain a config.json file
steps = 10000
seed = 3
N = 5

# Define map (X-OR problem)
h5f = h5py.File(dir+'/map.h5','w')
h5f.create_dataset('X', data=[0,0,1,1])
h5f.create_dataset('Y', data=[0,1,0,1])
h5f.create_dataset('Z', data=np.zeros(4))
h5f.create_dataset('F', data=[0,1,1,0])
h5f.close()

# Define network (N nodes, fully recurrent)
pre = []
post = []
pre, post = recur(pre,post,np.arange(N))
h5f = h5py.File(dir+'/network.h5','w')
h5f.create_dataset('pre', data=pre)
h5f.create_dataset('post', data=post)
h5f.close()

# Run the model
os.system('./../build/src/modelVis '+dir+' '+str(steps)+' '+str(seed))

print("run './../build/src/modelVis "+dir+" 0 0' to see the results")


