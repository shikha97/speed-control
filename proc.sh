#!/bin/sh
dir=$(pwd) 

alpr -c in $1 > $dir/saved_det.txt

python dostuff.py
