# Social Media

[Flask](http://flask.pocoo.org/docs/1.0/), is a web microframework for Python. It is mainly used to for web application development and also API development.

We create a [Social Media](https://en.wikipedia.org/wiki/Social_media) website using **Flask** and some of it's supporting extensions. Here, a user can:


1. Sign-up for the first time

2. Login using their credentials

3. Add new posts

4. Delete existent posts specific to that user

5. Can upload profile picture

6. Can view posts of other users

7. Logout of their accounts



## DBMS of Website

In this website we use [Object Relational Mapping](https://searchwindevelopment.techtarget.com/definition/object-relational-mapping) techniques using [SQL Alchemy](https://www.sqlalchemy.org/) on [sqlite3](https://docs.python.org/2/library/sqlite3.html) database for Python



## Extensions used


1. [flask-login](https://flask-login.readthedocs.io/en/latest/) for user session management of flask

2. [flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) is an extension for **SQLAlchemy** in Flask.

3. [flask-bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) is a Flask extension that provides bcrypt hashing utilities for our application. Used to hash user passwords before storing to database

4. [flask-wtf](https://flask-wtf.readthedocs.io/en/stable/) is simple integreation of **Flask** and [WTForms](https://wtforms.readthedocs.io/en/stable/). Provides easily applicable methods for creating web forms and also includes services like prevention against [CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)) attacks, reCAPTCHA, file upload etc.


## Reference

In my personal opinion [Corey Schafer](https://coreyms.com/development/python/python-flask-tutorials-full-series)'s Flask tutorial is better than even Udacity's full stack nano-degree.
