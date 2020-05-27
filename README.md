# flask-blog-api

## About

This is my first REST API I created in Flask. It's a simple blog API, that uses sqlite as a database. There are a total of four fields
for the title, author, content and image url for the author, but the fields are mutable by anyone who chooses to clone the repo and use it
locally.

## Usage

Clone the repo
  
Run `pipenv shell` to enter the python virtual environment.
  
Run `pipenv install` to install all the necessary packages in your vitual environment.
  
Run `python` to enter the python terminal to enter in python code. 
  
Run `from app import db` followed by `db_create_all()` this will create your local sqlite db for you by the schema you defined. **NOTE: You will have to run this command every time you modify the schema, otherwise you can just run it once and keep relaunching your local server when you like.**

Run `python app.py` to run the `app.py` file and launch your local server.

The server by default is hosted at `localhost:5000`

Use Postman to GET, POST, UPDATE or DELETE items in your database. 
  
You can later add your own front end with an HTTP client like `Axios` to make requests to your data in your front end. 
