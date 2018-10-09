#!/bin/bash

trap "exit" INT
for run in {0..100}
do
    python spaceinvaders1.py
done
