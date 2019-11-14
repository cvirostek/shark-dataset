#!/bin/bash

set -e

files=("$@")
length=$#
weights="weights/weights/darknet53.conv.74"

for (( i = 0; i < length; i++ )); do
  file="${files[i]}"
  echo "########## TRAINING SET $i ##########"
  python3 train.py --data "$file" --cfg cfg/yolov3-sharks.cfg --batch-size 8 --accumulate 1 --nosave --name "sharks-$i" --weights $weights --transfer
  weights="weights/sharks-$i.pt"
  mv weights/last.pt $weights
done

