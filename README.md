# CS2340 Movie Store
https://mahikaraj.pythonanywhere.com/ 

## About The Project
Objects and Design (CS 2340) course project with the goal of designing and developing a web application using Django that enables users to access information about movies and place orders to purchase them. This web application allows users to access information about movies and place orders to purchase them. Users will also be able to list, create, edit, and delete movie reviews. The application will feature a user-friendly interface and provide useful information about each movie, such as its name, price, description, and an image.

## Built With
- Django, a Python-based web framework
- HTML, CSS

## Learn about the Team and Process
https://cs2340pr1elias1.tilda.ws/

## Running the Website on Your Local Computer
# Prerequisites
1. Python (https://www.python.org/)
2. pip (https://pip.pypa.io/en/latest/installation/)
3. Django (https://www.djangoproject.com/)
   
# Installation
1. Clone the repo
   ```sh
   git clone https://github.com/li-kate/CS2340-Movie-Store.git
   ```
2, Install python-decouple to use .env files
      ```sh
      pip install python-decouple
      ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

# Creating the .env file
In /moviesstore (same folder location as manage.py), create a .env file and paste the following, and replace your email and your email password with your email and password.
   ```sh
  OUTLOOK_EMAIL= your email
  OUTLOOK_PASSWORD= your email password
   ```
**Note:** The variable says outlook, but if you are using a different emailing service, you just have to change the EMAIL_HOST in settings.py in /moviesstore/moviesstore to the SMTP server of the emailing service you are using.
   ```sh
  EMAIL_HOST = 'smtp.office365.com' // currently using Outlook
   ```

## Acknowledgments
This project follows the process featured in the textbook "Django 5 for the Impatient: Learn the core concepts of Django to develop Python web applications" by Dr. Daniel Correa and Mr. Greg Lim.
