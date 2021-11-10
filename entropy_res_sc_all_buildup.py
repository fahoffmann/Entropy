from pylab import loadtxt, remainder, hist
from math import log, pow
from sys import argv
from numpy import zeros, histogram

chi_nr=argv[3]
res_nr=argv[1]
res_name=argv[2]

cluster_size=3 #120
number_cluster=int(360/cluster_size)
nbins=int(pow(number_cluster,int(chi_nr)))

simlength=20000
length=20000
step=1 #write output every step times
nr_parts=15 #30

f1 = open('entropy_sc_res'+res_name+res_nr+'_all_'+str(cluster_size)+'_part_buildup_'+str(step),'w')
f2 = open('entropy_sc_res'+res_name+res_nr+'_all_'+str(cluster_size)+'_part_buildup_parts_'+str(step),'w')

quadrant=zeros((int(chi_nr),nr_parts,length))
cluster=zeros(length)

for j in range(1,int(chi_nr)+1):
    input_file='chi'+str(j)+res_name+res_nr+'.xvg'
    phi = remainder(loadtxt(input_file, unpack=True, usecols=[1]), 360)
    S=zeros((len(cluster)/(simlength/length)/step+1,nr_parts))
    for k in range(1,nr_parts+1):
        quadrant[j-1,k-1,:]=(phi[(k-1)*length:k*length]-remainder(phi[(k-1)*length:k*length],cluster_size))/cluster_size

S_avg=zeros(len(cluster)/(simlength/length)/step+1)
phi=[]
cluster=zeros((nr_parts,length))
for k in range(1,nr_parts+1):
    for j in range(0,int(chi_nr)):
        cluster[k-1]=cluster[k-1]+pow(number_cluster,j)*quadrant[j,k-1]
    for i in range(2,len(cluster[k-1])/(simlength/length)+2,step):
        for j in range(0,simlength/length):
            chis=cluster[k-1,j*length:j*length+i]
            his=histogram(chis.tolist(), bins=nbins, range=[0,nbins], normed=True)
            all_values=his[0]
            indices=all_values.nonzero()
            values=all_values[indices]
            S[(i-1)/step,k-1]=S[(i-1)/step,k-1]+sum([y*log(y) for y in values])
        S[(i-1)/step,k-1]=S[(i-1)/step,k-1]/(simlength/length)

for i in range(0,len(cluster[k-1])/(simlength/length)/step+1):
    S_avg[i]=sum(S[i,:])/nr_parts
    f1.write(str(i*step)+' '+str(res_nr)+' '+str(res_name)+' '+str(S_avg[i])+'\n')
    f2.write(str(i*step)+' '+str(res_nr)+' '+str(res_name)+' '+str(S[i,0:int(nr_parts/2)])+' '+str(S[i,int(nr_parts/2):nr_parts])+'\n')

f1.close()
f2.close()
