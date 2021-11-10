from pylab import loadtxt, fmod, hist
from math import log
from sys import argv
from numpy import zeros,histogram

res_nr=argv[1]

input_file='rama_bb'+res_nr+'.xvg'
cluster_size=20
number_cluster=360/20
nbins=number_cluster*number_cluster
nr_parts=15
step=1

#f = open('entropy_bb_res'+res_nr+'_part_buildup','a')
f1 = open('entropy_bb_res'+res_nr+'_part_buildup','w')
f2 = open('entropy_bb_res'+res_nr+'_part_buildup_parts','w')

phi, psi = loadtxt(input_file, unpack=True, usecols=[0,1])+180
length=len(phi)/nr_parts
quadrant=zeros((nr_parts,length))
S=zeros((length/step+1,nr_parts))
S_avg=zeros((length/step+1))

for k in range(1,nr_parts+1):
    quadrant[k-1,:]=number_cluster*(phi[(k-1)*length:k*length]-fmod(phi[(k-1)*length:k*length],cluster_size))/cluster_size+(psi[(k-1)*length:k*length]-fmod(psi[(k-1)*length:k*length],cluster_size))/cluster_size

for k in range(1,nr_parts+1):
    for i in range(1,length+2,step):
        his=histogram(quadrant[k-1,0:i], bins=nbins, range=[0,nbins], normed=True)
        all_values=his[0]
        indices=all_values.nonzero()
        values=all_values[indices]
        S[(i-1)/step,k-1]=sum([y*log(y) for y in values])

for i in range(0,length/step+1):
    S_avg[i]=sum(S[i,:])/nr_parts
    f1.write(str(i*step)+' '+str(S_avg[i])+'\n')
    f2.write(str(i*step)+' '+str(S[i,0:int(nr_parts/2)])+' '+str(S[i,int(nr_parts/2):nr_parts])+'\n')
    
f1.close()
f2.close()
