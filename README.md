# CryptoFiCalculator


## Introduction
Hi!
This is a Calculator App using Python Django, Bootstrap CSS, and jQuery. 

## Summary
This calculator app stores your calculations in a stack until you press the '=' button.
Upon hittin the '=' button, the app will make an AJAX call and send the stack to Python Django via a http GET request. 
The GET request will make the calculation and send the result back to the html page is show it in the 'display' of the calculator.

### I've kept the requirements minimum for this project by using references to CDN urls for 
 - Bootstrap CSS
 - jQuery

## Requirements

### You will need the following packages to run the solution: 
- asgiref==3.5.2
- Django==3.2.15
- pytz==2022.4
- sqlparse==0.4.3
- typing_extensions==4.3.0


## Setup

### You can set up the project by running the following commands :D

#### Using git bash, run the following command:
git clone https://github.com/Ali-Ismail-1/CryptoFiCalculator.git

#### Install django if you do not have it already 
pip install django==3.2.15

#### Open the folder CryptoFiCalculator and runt he following command to start the server:
python .\manage.py runserver

#### View the Calculator app using the following url:
http://127.0.0.1:8000/calculatorapp/



## Reproduction

### Just in case you want to follow my set up steps from scratch, here's the commands I used in my terminal
- django-admin startproject CryptoFiCalculator
- pip install virtualenv
- virtualenv myenv
- myenv\Scripts\activate
- pip install django
- python .\manage.py startapp calculatorapp
- python .\manage.py migrate
- pip freeze > requirements.txt
- python .\manage.py runserver
