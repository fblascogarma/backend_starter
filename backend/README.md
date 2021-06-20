# Build a backend using Django (Python framework)

This project will teach you how to quickly build a backend for your web app using Django which is one of the most popular frameworks for backend development. Follow the steps and test it afterwards to see that it works properly. 

When you finish, you can use this project to customize it for your needs by creating your models, views (logic you want to apply on the backend with the info from your frontend), and API endpoints to communicate with your frontend.

If you want to learn different ways of setting your backend using Django, check out the references for more resources.

## Steps

1) Create a virtual environment and activate it.
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
 
4) Learn how people are responding to a new important update or new feature release.
5) It will help you build your product competitive matrix and segment customers.
6) Learn how a new marketing campaign is resonating with your target customers.
7) Help you determine the marketing strategy of a new product launch.
8) Also helpful to decide how to position your product to different segments.
9) Learn about a new market entry opportunity.

## About this project

This project aims to analyze customer reviews of Alexa products using NLP and ML in Python, but it can be used to analyze other sources like social media posts, user reviews on Play Store & App Store, and internal customer feedback data like CSAT or NPS responses.
I got the dataset from [Kaggle](https://www.kaggle.com/sid321axn/amazon-alexa-reviews) and did some changes so it is more versatile and you can use it for multiple products/apps. The dataset is on reviews.csv file and after running absa.py the program will create an Excel file called Alexa.xlsx. 
We are using a small dataset of 3.150 reviews but you can use a much larger one.

## References

1) Video tutorial called [Django & ReactJS Full Stack Course [ Python Backend React Frontend ]](https://www.youtube.com/watch?v=VBqJ0-imSMU)
2) [Serializer documentation](https://www.django-rest-framework.org/tutorial/1-serialization/)

## Why do we need to create a virtual environment

The virtual environment is something you create when you start a project. It's always advisable to create a virtual environment for your new project so the libraries you install there don't conflict with your other projects that might demand other versions of the libraries. For example, I am using vaderSentiment version 3.3.2 for this project, but for another project, I might need vaderSentiment version 3.2.5.

To create a virtual environment in Python 3 and using VS Code as your IDE, write this in the terminal:
py -3 -m venv name_of_project
In my case, the name_of_project is demo_gh
Go to the folder that contains the virtual environment folder
And to activate the virtual environment type
name_of_project\Scripts\activate
You will see in parenthesis (name_of_project) before the path if you successfully activated the virtual environment.