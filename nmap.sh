#!/bin/bash

B0="$(printf '\033[100m')" S0="$(printf '\033[30m')"
B1="$(printf '\033[91m')" S1="$(printf '\033[31m')"
B2="$(printf '\033[92m')" S2="$(printf '\033[32m')"
B3="$(printf '\033[93m')" S3="$(printf '\033[33m')"
B4="$(printf '\033[94m')" S4="$(printf '\033[34m')"
B5="$(printf '\033[95m')" S5="$(printf '\033[35m')"
B6="$(printf '\033[96m')" S6="$(printf '\033[36m')"
B7="$(printf '\033[97m')" S7="$(printf '\033[37m')"
R1="$(printf '\033[0;1m')" R0="$(printf '\033[00m')"


warn='\033[0;31m'
reset='\e[0m'

echo -e -n "${warn}Enter the Domain: ${reset}"
read choice

#read -p 'Enter the Domain:' webv
echo $B4
nmap -sV $choice