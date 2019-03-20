# pro_web_scraping

[2019.03.20-ubuntu]
download chrome linux
cd project/
sudo apt install git
sudo apt install vim

vim ~/.bash_aliases
alias ae='deactivate &> /dev/null; source ./venv/bin/activate'
alias de='deactivate'

sudo apt install virtualenv
virtualenv -p /usr/bin/python3 env
sudo pip install python-pip
pip install selenium
pip install requests
pip freeze --local > requirements

download google web driver
- move driver into PATH
mv chromedriver ./env/bin

