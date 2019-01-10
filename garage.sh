#!/bin/bash

trigger_file_open="/home/james/Dropbox/ifttt_commands/open_garage.txt"
trigger_file_close="/home/james/Dropbox/ifttt_commands/close_garage.txt"

if [[ -f ${trigger_file_open} ]]
then
  rm ${trigger_file_open}
  /home/james/scripts/open_garage.py
fi

if [[ -f ${trigger_file_close} ]]
then
  rm ${trigger_file_close}
  /home/james/scripts/close_garage.py
fi

#sleep 10
#pgrep chrom |xargs kill -9
