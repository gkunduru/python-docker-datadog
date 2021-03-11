from ddtrace import tracer
from ddtrace import config
import requests
import os
import time


# change the service name
session = requests.session
cfg = config.get_from(session)
cfg['service_name'] = 'python_long_running_service'


def initiate_process() :
    while True :
        print ("process got initiated")
        sample_url="https://earthquake.usgs.gov/fdsnws/event/1/application.json"
        try:sample_response = requests.get(sample_url)
        except:
            print({"message_type" : "Error", "message" : "Connection to a EarthQuake API failed. Trying again..."})            
        if(sample_response.status_code==200) :
            print({"message_type" : "Info", "message" : "Connection Succeeded to a EarthQuake API"})
        time.sleep(5)



if __name__ == "__main__":
    initiate_process()
