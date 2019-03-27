# pro_web_scraping
- Getting started
```./setup.sh```

[youtube embed video]  
We need to scrap [video_ID]
example code snippet:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/[video_ID]" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  

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

##Download web driver##
- Fiefox  
https://github.com/mozilla/geckodriver/releases  
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz  
tar -xvzf *.tar.gz  
chmod +x geckodriver  
export to PATH  

- move driver into PATH    
mv chromedriver ./env/bin    

