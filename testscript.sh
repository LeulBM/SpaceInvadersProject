#!/bin/bash

trap "exit" INT
for run in {1..100}
do
    python twitchagent.py
done
