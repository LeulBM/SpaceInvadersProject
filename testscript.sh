#!/bin/bash

trap "exit" INT
for run in {0..100}
do
    python space_invaders.py
done
