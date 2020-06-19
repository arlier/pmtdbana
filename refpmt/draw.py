import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

with open("pmtdb.txt", "r") as f:
	data = f.readlines()
	mup1=[] #mu@0.1pe
	mu1=[] #mu@1pe
	time=[]
	pde=[]
	for i in range(0,len(data)):
		data[i]=data[i].strip('\n').split('\t')
		if float(data[i][8])>3 or float(data[i][8])<.3:
			continue
		if float(data[i][5])>.3 or float(data[i][5])<.03:
			continue
		if int(data[i][14])!=101:
			continue
		mup1.append(float(data[i][5]))
		mu1.append(float(data[i][8]))
		pde.append(float(data[i][9]))
		ftime=datetime.strptime(data[i][3],'%Y-%m-%d').date()
		time.append(ftime)
	print(data[0])
	print(len(data))
arraymup1=np.array(mup1)
arraymu1=np.array(mu1)
arraypde=np.array(pde)/28.
arraymup1_10=arraymup1*10


figmu=plt.figure(0,figsize=(15,8))
ax=figmu.add_subplot(111)
plt.plot(time,arraymu1)
plt.plot(time,arraymup1_10)
plt.grid(ls=":",c='k')
plt.xlabel('time',fontsize=20)
plt.ylabel(r'$\mu$@0.1pex10 &setpoint 3000',fontsize=20)
ax.legend([r'$\mu$@setpoint3000',r'$\mu$@0.1pex10'])
plt.savefig("test.png")
figpde=plt.figure(1,figsize=(15,8))
ax1=figpde.add_subplot(111)
plt.plot(time,arraymu1)
plt.plot(time,arraymup1_10)
plt.plot(time,arraypde)
plt.grid(ls=":",c='k')
plt.xlabel('time',fontsize=20)
plt.ylabel(r'$\mu$@0.1pex10 &setpoint 3000',fontsize=20)
ax1.legend([r'$\mu$@setpoint3000',r'$\mu$@0.1pex10','PDE@setpoint3000/28'])
plt.savefig("testpde.png")
