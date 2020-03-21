#!/bin/bash
sudo apt install python3.6
#sudo apt install pip3
sudo apt-get install python3-pip
sudo apt install pip
sudo apt install virtualenv
sudo apt install virtualenvwrapper

sudo pip3 install -H virtualenv virtualenvwrapper

add to .bashrc
export WORKON_HOME=$HOME/.virtualenv
export VIRTUALENVWRAPPER_LOG_DIR="$WORKON_HOME"
export VIRTUALENVWRAPPER_HOOK_DIR="$WORKON_HOME"
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh


cd ~
mkvirtualenv -p /usr/bin/python3.6 pwp
workon pwp

git clone https://github.com/Diamante-GIT/practicewithpros.git
sudo chmod 777 -R ./prac*

mkdir static
mkdir static/home

cd Client-Dashboard
pip3 install -r ./requirements.txt
export DJANGO_SETTINGS_MODULE="BLM.settings.production"
export DJANGO_SETTINGS_MODULE="home.settings.development"

python manage.py collectstatic
python manage.py makemigrations SSO
python manage.py makemigrations cuser
python manage.py migrate

echo 'run these commands to execute server:'
echo 'cd /home/Client-Dashboard'
echo 'workon BLMLIVE'
echo 'export DJANGO_SETTINGS_MODULE="BLM.settings.production"'
echo 'python manage.py runserver 0.0.0.0:8080 --insecure --setting BLM.settings.production'

