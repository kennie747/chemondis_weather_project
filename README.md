# chemondis_weather_project
The CheMondis Weather Project for getting the weather situation in any city of interest

While containerizing (dockerizing) the application has been plagued with the redis server refusing to respond to requests, 
the application itself is complete and running fine if executed in the following steps:

1. Install redis server: sudo apt-get install redis-server 
2. Run the redis server : sudo service redis-server restart 
3. Run the program: 
    i. pip install -r requirements.txt
    ii. python manage.py runserver
    
Kindly bear with me while I work on fixing the container issue
 
