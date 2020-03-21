#!/bin/bash
echo 'THIS SCRIPT REQUIRES ~/movie.MP4 (in the home directory - it is too large to put on the Git Repo)'
echo 'Killing current dev server'
echo 'Removing old PWP0, moving current PWP to PWP0, cloning new PWP'
echo 'Starting virtualenv, running dev server'
cd ~
sudo pkill python3.6
sudo rm -R practicewithpros0
sudo mv practicewithpros practicewithpros0
git clone https://05ac659ac6a28b2481a2e07fb529af42cb1dff6b@github.com/Diamante-GIT/practicewithpros.git
echo 'Copying in movie file'
sudo cp movie.MP4 practicewithpros/static/home/videos/
cd practicewithpros
sudo chmod -R 777 .
workon pwp
sudo ~/.virtualenv/pwp/bin/python3.6 manage.py runserver 0:80 &>/dev/null &
#replace &>/dev/null & with just & if you want output to pipe to terminal (annoying imo)
deactivate
cd ~
jobs
disown
echo ''
ls