#!/bin/bash
# My first script

echo "Step1. Setup python virtual env and activate"
echo "Step2. Install all the python dependencies"
echo "Step3. Download web driver"
echo "Step4. Move web driver to PATH of python virtual env"
echo "Step5. Run web scraping python script"


echo "Enter c if using Google Chrome. Enter f if using Firefox"
read browser

if [ $browser == 'c' ];
then	
	echo "Download chromedriver"
elif [ $browser == 'f' ];
then
	echo "Download geckodriver"
else
	echo "Please type in 'c' or 'f'"
fi

: '
echo "Step2. Setup python virtual env"
if [ -d "$env" ]
then
    echo "Set up a python virtual environment"
else
	echo "python virtual environment is already in env/"
fi
'

echo "Finish setup in your linux system"

#===========================================
#Note
#multi-line comment  : ' ABCD '
