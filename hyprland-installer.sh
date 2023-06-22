#!/bin/bash

###################################################
#												  #
#            Author: Maxim Timofeev               #
#                                                 #
###################################################

{
echo -e "Installer Hyprland Wayland\nInstall? (y/N)?"
read answer
    if [[ $answer = [sSyY] ]]; then
        echo -e "\nStart installing...\n"

        yay -S brightnessctl bluez chromium kitty thunar code swaybg swayidle swaylock wlroots wl-clipboard waybar-hyprland-git wofi foot mako grim slurp light yad obs-studio imagemagick nwg-look xorg-xwayland wps-office swww
        
        echo -e "\nInstall hyprland\n"
        
        yay -S hyprland-git       
        yay -S wlrobs-hg
        
        sleep 3
        echo -e "\nCreate dirs\n"
        mkdir -p ~/.config/hypr
        mkdir -p ~/.config/waybar
        echo -e "\nCopy files in new dirs\n"
        cp -r hypr/* ~/.config/hypr/
        cp -r waybar/* ~/.config/waybar/
        echo -e "\n...Complete\n"
    else
        echo -e "\nOkey/ Goodbuy\!\n"
    	exit 0
    fi
}
