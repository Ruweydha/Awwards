# Awwards

## A Description of the WebApplication.
A website where users can post their projects and they can be rated in terms of design, content and userbility

## Table of Content

+ [Description](#description)
+ [Behaviour Driven Development](#behaviour-driven-development)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description

<p>A website where users can post their projects and they can be rated in terms of design, content and userbility</p>

## Behaviour Driven Development

<p>

* A user can Sign in to the application to start using.
* A user can upload projects to the application to be rated.
* As user can see their profile with all their projects.
* A user can see other projects posted on the time and they can rate them too.

</p>

***
## Installation

* Open Terminal `ctrl+Alt+T`

* Git clone https://github.com/Ruweydha/Awwards

or

* Git fork - Enter into your own repository and search-https://github.com/Ruweydha/Awwards then click on fork to add
it on your own repository.

 Navigate into the cloned project. 
`cd Awwards`


* Create and activate the vitual Environment and install the from requirements.txt
`$ python3.8 -m virtualenv virtual`
`$ source virtual/bin/activate`
`$ pip install -r requirements.txt`

* Setting up environment variables

Create an `.env` and add the following.
```
SECRET_KEY='<Secret_key>'
DBNAME='<DbName>'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1

```

requirements from 
---
```
$ python3 -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt

```
Perform a migration
```
python3 manage.py migrate

```


* Start the Server to run the app
* `$ python3 manage.py runserver`

* Open [localhost:8000](#)
***


### Requirements

* Either a computer,phone,tablet or an Ipad

* An access to the Internet

* Python3

* Postgres

* virtualenv

* Pip


## Technology Used

* HTML 5 - which was used to build the structure of the pages.

* CSS - which was used to style the pages incuding the left aside navigation bar.

* Figma-which was used to design the prototype of the UI.

* Python/Flask - Which was used to build the web-applications and interactivity

* Postgresql - For the database

* Heroku - For deployment

## Reference

* LMS
* W3schools
* stackOverFlow


## Licence

MIT License

Copyright (c) [2022](#licence) [Ruweydha Abdinoor](#licence)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors Info


Linked - [Ruweydha Abdinoor](https://www.linkedin.com/in/ruweydha-abdinoor-859921224/)

Gmail - [ruweydha.abdinoor@student.moringaschool.com]()

Github - [Ruweydha](https://github.com/Ruweydha)
