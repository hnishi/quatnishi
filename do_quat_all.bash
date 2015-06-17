#!/bin/bash

################################################################################
# function : bash
# description : 
################################################################################
file="prm.inp"
ex_quatnishi="./quatnishi"
iend=64
dir="/work1/hnishi/4thTrial/ama2/md/md17"

#iend=`wc $file | cut -d' ' -f-10`
#iend=`wc -l $file | cut -d' ' -f 1`
#mkdir $dir/list_stru

echo total number of trajectories = $iend

#echo 74 > aaa.inp
#rm aaa.inp
 
rm out_rmsd_all.dat
touch out_rmsd_all.dat
for (( i=1; i<=$iend; i++ ))
do
   sed -e "s;__CODNAME__;$dir/no$i/mdx.crd;" -e "s;__RMSDFILE__;out_rmsd;" $file > aaa
   $ex_quatnishi aaa > aaa.log
   cat out_rmsd >> out_rmsd_all.dat
   rm out_rmsd
   wc -l out_rmsd_all.dat
done

rm aaa aaa.log

echo end
#ls $dir/list_stru
