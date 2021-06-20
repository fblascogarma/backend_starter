# Build a backend using Django (Python framework)

This project will teach you how to quickly build a backend for your web app using Django which is one of the most popular frameworks for backend development. Follow the steps and test it afterwards to see that it works properly. 

When you finish, you can use this project to customize it for your needs by creating your models, views (logic you want to apply on the backend with the info from your frontend), and API endpoints to communicate with your frontend.

If you want to learn different ways of setting your backend using Django, check out the references for more resources.

## Steps

1) Create a virtual environment and activate it. If you don't know why this is necessary, check the last section of this file.

2) Install Django by typing
pip install Django
Also install Django REST framework by typing
pip install djangorestframework
You need to create a Django project by typing
django-admin startproject NAME_OF_BACKEND_PROJECT
Choose the name that you like. For this project, the name is backend.
 
3) Start the server by navigating to the NAME_OF_BACKEND_PROJECT folder and type
python manage.py runserver
To check that the server is running properly, in a new tab in your browser go to
http://localhost:8000/
You should see a spaceship and say the installation worked successfully.
![alt text](images/Installation_ok.PNG)
 
4) Migrate data to the db by navigating to your NAME_OF_BACKEND_PROJECT folder and typing
python manage.py migrate
Make sure you have the venv activated. You will see something like this:
![alt text](images/migrate_first_one.PNG)

Every time you want to migrate data to your database, you have to run that command.
The default db is SQLite but you can change that.

5) To create an API for your app, type

python manage.py startapp api

You need to create an admin user by typing

python manage.py createsuperuser

And you will need to input the username you want to create, an email, and a password.

6) Create a urls.py file in api folder and paste this (check the file in this repo if you want to copy paste; the same with all the rest).

![alt text](images/urls_in_api.PNG)

7) Go to the urls.py file in the NAME_OF_PROJECT folder and delete what you have there and paste this that will add that new urls.py file from the previous step and also add authentication so only authorized users can call the api.
![alt text](images/urls_in_project.PNG)

8) Go to models.py in api folder, delete what you have there, and create a model by pasting this
![alt text](images/models.PNG)

9) Register the model created in admin.py in api folder by pasting
![alt text](images/admin.PNG)

10) Create a serializers.py file in the api folder and paste this
![alt text](images/serializers.PNG)

A model serializer is preferred over a serializer because it’s more succinct and clear to read. ModelSerializer will automatically generate a set of fields for you based on your model and validators for the serializer.

11) Go to settings.py in NAME_OF_PROJECT folder and add rest_framework, rest_framework.authtoken, and api under INSTALLED_APPS:

![alt text](images/installed_apps.PNG)

The rest_framekwork.authtoken is to prevent unauthorized users from creating/deleting/editing information in our backend.

12) Go to views.py in api folder and paste this
![alt text](images/views.PNG)

13) Go to the folder where you have your backend folder project and type 
python manage.py makemigrations
You should see something like this
Migrations for 'api':
  api/migrations/0001_initial.py
    - Create model Article

Which states that the model Article was created successfully. 

14) To push it to the database, type
python manage.py migrate
And you will see something like this
![alt text](images/migrate.PNG)

15) If you go to the admin panel, you will see the model Articles created and the tokens for authentication:
![alt text](images/admin_panel.PNG)

Click on Tokens > Add token, select a user and click save. You will see a token created for that user. Therefore, only that user with that token will be able to see the viewset and interact with the model. 

16) Test that your new backend works correctly by using [Postman](https://www.postman.com/). 
Create a new workspace and put http://localhost:8000/api/users/ with a POST call and you should get a response with a 400 bad request error saying that username and password are required:
![alt text](images/bad_request.PNG)

Go to Body in Postman, select form-data, and add username and password in KEY column and select a new username to be created and a password. You should get 201 created response with the new username created, without showing you the password value.

![alt text](images/201_response.PNG)

Now, go to your admin panel in localhost:8000 and go to Users to see the new user created.
![alt text](images/user_created.PNG)

Go to Tokens to see that a token has been created automatically for that new user.
![alt text](images/token_created.PNG)

Now, change the call to a GET and the url to http://localhost:8000/api/articles/ and you should get a 401 unauthorized error response because you didn’t provide credentials.
![alt text](images/401_unauthorized.PNG)

Go to Headers in Postman, add Authorization in KEY column and in VALUE column write Token and paste the token of the new user created. Now, you should be able to get the articles because you are using the credentials of an authorized user. You know it worked correctly if you get a 200 response.
![alt text](images/200_response.PNG)

You are all set! Customize it for your web app. Read the next section to have a better understanding of this framework.

## About Django's framework

The models.py file is where you will create the models to use in your backend. For example, if you have a sign-up for newsletters, you will need a model with the fields that the user completes when signing up. 

The admin.py file is to register each new model you create.

The serializers.py file is to create serializer functions for your new models.

The views.py file is to create the view of your new model. Don't forget to import the new serializer function you created for this model in the serializers.py file.

The urls.py file in the api folder is to register endpoints so front can send data to back, and viceversa. 

Don't forget to migrate the information after creating a new model by navigating to the folder that contains the manage.py file and type
python manage.py makemigrations
And then type
python manage.py migrate

## References

1) Video tutorial called [Django & ReactJS Full Stack Course [ Python Backend React Frontend ]](https://www.youtube.com/watch?v=VBqJ0-imSMU)
2) [Django documentation](https://docs.djangoproject.com/en/3.2/)
3) [Serializer documentation](https://www.django-rest-framework.org/tutorial/1-serialization/)

## Why do we need to create a virtual environment

The virtual environment is something you create when you start a project. It's always advisable to create a virtual environment for your new project so the libraries you install there don't conflict with your other projects that might demand other versions of the libraries. For example, I am using vaderSentiment version 3.3.2 for this project, but for another project, I might need vaderSentiment version 3.2.5.

To create a virtual environment in Python 3 and using VS Code as your IDE, write this in the terminal:
py -3 -m venv name_of_project
In my case, the name_of_project is demo_gh
Go to the folder that contains the virtual environment folder
And to activate the virtual environment type
name_of_project\Scripts\activate
You will see in parenthesis (name_of_project) before the path if you successfully activated the virtual environment.
If you are using shell, to activate the venv you type source name_of_project/bin/activate