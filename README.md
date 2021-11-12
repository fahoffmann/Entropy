# Entropy
Entropy calculation from GROMACS backbone and side chain trajectories

There are two scripts for the calculation of the residual entropy from the protein backbone (entropy_res_bb_buildup.py) and sidechain (entropy_res_sc_all_buildup.py). They were used for the calculation of the entropy in this paper:

http://doi.org/10.33774/chemrxiv-2021-l686w

The sidechain script is used as a simple python program:
python entropy_res_sc_all_buildup.py ${res_nr} ${res_name} ${chi_nr}
Here, ${res_nr} ${res_name} and ${chi_nr} are the residue number, the residue name and the number of side chain dihedral angles of this side chain, e.g.
python entropy_res_sc_all_buildup.py 12 MET 3
for the side chain entropy of residue MET12. The script assumes to find all sidechain chi trajectory of this residue from the GROMACS gmx chi -rama command without the lines starting with "@" in the same folder, e.g. chi1MET12.xvg, chi2MET12.xvg and chi3MET12.xvg in the example above. The bin size can be set manually in the script (dafault: 10 degrees). The block size for the entropy calculation can also be set in the script (default: 20000 time steps, e.g. 20 ns if you save the trajectory every 1 ps).
Output is a file with with four colums: 
${time} ${res_nr} ${res_name} ${entropy}

The backbone script is used similar:
python entropy_res_bb_buildup.py ${i}
Here, ${i} is the residue number, e.g.
python entropy_res_bb_buildup.py 12
for the backbone of MET12. The script assumes to find the backbone dihedral trajectories of this residue in a file rama_bb${i}.xvg in the same folder. This file can be created by running the provided convert.sh script in a folder, in which the phi*.xvg or psi*.xvg files are loacted. These files are the outputs of the GROMACS gmx chi -rama command.
Output is a file with with two colums: 
${time} ${entropy}
