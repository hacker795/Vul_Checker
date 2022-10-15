trap 'printf "\n";stop;exit 1' 2


dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Install it. Aborting."; exit 1; }

}
echo 'Enter the Onion Link: '
read -p $'>>=>\e[0m\en' onion
 
docker run --rm -it milesrichardson/onion-nmap  -sV -p 21,80,443,139,3389 $onion


banner
dependencies
menu