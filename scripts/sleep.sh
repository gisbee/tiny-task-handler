#!/bin/bash

while [[ "$#" -gt 0 ]]; do
  case $1 in
         --welcometext      ) welcometext=$2; shift;;
         --seconds          ) seconds=$2; shift;;
         --exittext         ) exittext=$2; shift;;
    -h | --help             ) helper; exit 0; shift;;
    *                       ) echo "Error: Unknown parameter passed: $1";
                              echo; helper; exit 1; ;;
  esac; shift;
done

echo $welcometext
sleep $seconds
echo $exittext
