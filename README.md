
# Problem Statement:

Go through the sample JSON file given here -
https://drive.google.com/open?id=1xZa3UoXZ3uj2j0Q7653iBp1NrT0gKj0Y
This JSON file describes a list of users &amp; their corresponding periods of activity across
multiple months.

Now, design and implement a Django application with User and ActivityPeriod models, write
a custom management command to populate the database with some dummy data, and design
an API to serve that data in the json format given above.


# Development steps:

  Run requirements.txt file to install the requirements of the application::

    $ pip install -r requirements.txt

  Create django project Test and application FTLapp under that::
  
    $ python manage.py startproject Test
    $ python manage.py startapp FTLapp
    
  Create User and ActivityPeriod models in FTLapp and do makemigrations and migrate to create respective tables::
  
    $ python manage.py makemigrations FTLapp
    $ python manage.py migrate FTLapp
    
  Do migrate to create django inbuilt migrations to create dependency tables::
  
    $ python manage.py migrate
    
  Follow the below heirachy of folder/file creation to create custom management commands::
   
  Implement custom commands to create users. There are two files been created for two commands which can be used to add single user with specific data and to add bulk users with   dummy data. 
  Below is the command **adduser** followed by *id* *real_name* *tz* and the argument *--start_time* followed by one/more values of it and the argument *--end_time*               followed by one/more values of it which is to be used for to create single user ::
  
     $ python manage.py adduser W07QCRPA4 Glinda_Southgood Asia/Kolkata --start_time Feb-1-2020-1:33PM Mar-1-2020-1:33PM Apr-1-2020-1:33PM --end_time Feb-1-2020-5:33PM Mar-1-        2020-5:33PM Apr-1-2020-5:33PM
     
  Below is the command **addbulk** followed by an integer value(total number of users) which is to be used for to create bulk of dummy users ::   
  
    $ python manage.py addbulk 10
    
  As the users got created and populated in DB, Need to create API to get them as json. Below command to create app for API::
  
    $ python manage.py startapp FTLapi
    
  Import the models of FTLapp into FTLapi and create serializers.py file to create modelserializers. Later import the created serializers into views.py file and use viewset to     list available users in the DB as a jsonfile. To add authenetication to it, create superuser and password which is basic authentication (Token authentication also can be         done)::
  
    $ python manage.py createsuperuser
    
  It'll ask for **username**, **email-ID**, **password** .Once confirm them, run the server by below command::
  
    $ python manage.py runserver http://127.0.0.1:8080
  
  If we open the URL in browser and go to *http://127.0.0.1:8080/api/* It'll asks for username and password which has been given in prior step. Once authenticated It'll display   the list of users in the browser as like in the given json format. 
  
  We can make changes to users and their activity periods via UI if we goto the link *http://127.0.0.1:8080/admin/* as I have registered the User and ActivityPeriod models to     the admin site.
     
< img src="https://github.com/gowthamimanchuri517/FTL-Assignment/blob/master/Images/api_results.PNG">
