# chemondis_weather_project
The CheMondis Weather Project for getting the weather situation in any city of interest

This is a complete working solution for checking the weather condition in any city.

I had some challenges with the very last component of the requirements, that is, running the program by using docker-compose. The Redis Cache fails to respond to connection requests after containerization and running with docker-compose. So, while the program runs with the docker-compose instruction, an error occurs while trying to perform caching.

While running the application with docker-compose has been plagued with the redis server refusing to respond to requests, 
the application itself is complete and running fine if executed in the following steps:

1. Install the redis server by executing the instruction: sudo apt-get install redis-server 
2. Run the redis server by executing the instruction: sudo service redis-server restart 
3. Navigate to the working directory and run the program by executing the following instructions: 
    i. pip install -r requirements.txt
    ii. python manage.py runserver
    
Kindly bear with me while I work on fixing the docker-compose issue.
 
