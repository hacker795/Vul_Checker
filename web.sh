#!/bin/bash


echo -e """
\e[38;5;197m ꧁෴╔══════════════════❖•ೋ°៚°ೋ•❖══════════════════╗෴꧂
\e[1;91m    ➣Name       ⇶   StranArmy
\e[38;5;197m ꧁෴╚══════════════════❖•ೋ°៚°ೋ•❖══════════════════╝෴꧂
\e[1;93m               

              
"""
 read -p $'Enter the WebSite Name:' opv
 
 python3 webscan.py $opv
 echo -e "\033[1;95m[\033[1;97mq\033[1;95m] \033[1;97m\033[1;101mQuit\033[0m"

 echo -e -n "\e[38;5;47m\e[38;5;197mStranArmy:~# "
read option
echo ""
case $option in
    q ) exit ;;
    * ) tput setf 4;echo -n "StranArmy:~#: ";tput setf 4;
esac
done
 }
main_menu




