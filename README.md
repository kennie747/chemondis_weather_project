# chemondis_weather_project
The CheMondis Weather Project for getting the weather situation in any city of interest

This is a complete working solution for checking the weather condition in any city.

I had some challenges with the very last component of the requirements, that is, running the program by using docker-compose. "docker-compose up" works just fine, but the user should leave the caching time-out at 0 so as to bypas the cache. The Redis Cache fails to respond to connection requests after containerization and running with "docker-compose up". So, while the program runs with the docker-compose instruction, an error occurs while trying to perform caching, hence the need to leave the cache-timeout value at 0 for now, while the issue is being fixed.

While running the application with docker-compose has been plagued with the redis server refusing to respond to requests, 
the application itself is complete and running fine with all caching and asyncio working properly if executed in the following steps:

1. Install the redis server by executing the instruction: sudo apt-get install redis-server 
2. Run the redis server by executing the instruction: sudo service redis-server restart 
3. Navigate to the working directory of the CheMondis_weather_project and run the program by executing the following instructions: 

    i. pip install -r requirements.txt
    
    ii. python manage.py runserver
    
 
##########################################################################

ALTERNATIVELY:

Navigate to the working directory of the CheMondis_weather_project and run the program by executing the following instructions: 

Execute the following commands to build the docker images and run them respectively: 

    i. docker-compose build

    ii. docker-compose up

However as earlier explained, the user should leave the configuration settings of the cache timeout at 0.
If the cache timeout setting is changed by the user to some other value, the application does not respond properly for now.


Kindly bear with me while I work on fixing the issue.

Thank you for your understanding.
