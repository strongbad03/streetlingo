#!/bin/bash

## Ubuntu only
## install Git and Python
#echo "Installing Python..."
#sudo add-apt-repository ppa:deadsnakes/ppa
#sudo apt update
#sudo apt install python3.6 -y
#sudo apt install firefox -y
#echo "Python installed. Configuring Git..."

# Git config
#ssh-keygen -t ed25519 -b 2048 -t rsa -f /home/ubuntu/.ssh/id_ed25519 -q -N ""
#eval "$(ssh-agent -s)"
#ssh-add ~/.ssh/id_ed25519
#cat ~/.ssh/id_ed25519.pub
#echo "===================
#COPY SSH KEY UP TO GITHUB NOW
#==================="
#sleep 30
#touch ~/.ssh/known_hosts
#ssh-keygen -F github.com || ssh-keyscan github.com >>~/.ssh/known_hosts
#git clone git@github.com:strongbad03/streetlingo.git
#cd streetlingo
#sudo chmod 700 bootstrap.sh
#echo "Repo cloned, starting boostrap."
#./bootstrap.sh

# install Pip, virtualenv, and create venv
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.6 get-pip.py
python3.6 -m pip install virtualenv
python3.6 -m virtualenv streetlingo ~/venvs/streetlingo/
source venv/streetlingo/bin/activate
pip install -r requirements.txt
python3.6 main.py

# TightVNC
sudo apt install ubuntu-desktop -y
sudo apt install tightvncserver -y
sudo apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal -y
vncserver :1
\cp ./xstartup ~/.vnc/xstartup
vncserver -kill :1
vncserver :1

# install QGIS
sudo apt install gnupg software-properties-common
wget -qO - https://qgis.org/downloads/qgis-2020.gpg.key | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import
sudo chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg
sudo add-apt-repository "deb https://qgis.org/debian `lsb_release -c -s` main"
sudo apt update
sudo apt install qgis -y