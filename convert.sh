#!/bin/bash

file_list=file_list
bin_width=20
number_of_bins=360/${bin_width}

if [ -f ${file_list} ]; then rm ${file_list}; fi
for file in `ls phi*.xvg`;
do
  file_base=`basename ${file} .xvg`
  file_number=`echo ${file_base} | grep -o "[0-9]\+"`
  psi_file=`echo ${file_base} | sed "s/phi/psi/g"`
  echo ${file_number}" "${file_base}" "${psi_file} >> ${file_list}
done
sort -n ${file_list} >> test; mv test ${file_list}
for file_base in `awk '{print $2}' ${file_list}`;
do
  phi_file=${file_base}".xvg"
  psi_file=`echo ${phi_file} | sed "s/phi/psi/g"`
  file_number=`echo ${file_base} | grep -o "[0-9]\+"`
  sed "/@/d" ${phi_file} | sed "/#/d" | awk '{print $2}' > test1
  sed "/@/d" ${psi_file} | sed "/#/d" | awk '{print $2}' > test2
  paste test1 test2 > rama_bb${file_number}.xvg
done
rm test1
rm test2
