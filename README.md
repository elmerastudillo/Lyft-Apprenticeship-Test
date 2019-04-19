# lyft-apprentice-test

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A web application built for Lyft's Software Engineer Apprenticeship with the following specifications:
```
Write a small web application in one of the above languages (Python/Ruby/Node).
It only needs to accept a POST request to the route “/test” which accepts one argument “string_to_cut” 
returns a JSON object with the key “return_string” and a string containing every third letter 
from the original string. E.g. if you POST {"string_to_cut": "iamyourlyftdriver"}, it will
return: {"return_string": "muydv"}. To see expected behavior you can test against a 
current working example with the command: 
curl -X POST https://lyft-interview-test.herokuapp.com/test --data 
'{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
## Demo
To use the Heroku live demo open your favorite command line and paste the following:
```
curl -X POST https://lyft-apprentice-test.herokuapp.com/test --data '{"string_to_cut": "ineedalyft!"}' 
-H 'Content-Type: application/json'
```
Note: Change the value assigned to `string_to_cut` to test with your own input.

## Installation
We use [pip](https://pip.pypa.io/en/stable/) for package management and [virtualenv]((https://virtualenv.pypa.io/en/latest/)) for our virtual environment. This should be installed before continuing.

1. Clone the project with:
```
https://github.com/elmerastudillo/Lyft-Apprenticeship-Test.git
```
2. In the root directory of the project set up your virtual environment with the following command, replacing `venv-name` with any name you choose for your virutal environment.
```
sudo virtualenv venv-name
```
3. Install Flask with the following commands, replace `venv-name` with your chosen virtual environment name.
 ```
source venv-name/bin/activate
sudo pip install Flask
 ```
 4. Now for the last step, install all packages with the following command:
 ```
 pip install --upgrade -r requirements.txt
 ```
## Usage

Once installation is done, you can run the application using the following command:
```
flask run
```
To test the application use the following command:
```
curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "ineedalyft!"}' 
-H 'Content-Type: application/json'
```



## License

![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)
