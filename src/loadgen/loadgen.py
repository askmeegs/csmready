import threading
import datetime 
import schedule
import os 
import time
import grequests 

def exception_handler(request, exception):
    print("Request failed: %s" % exception)


def callserver(): 
    urls = [url]*c  # number of concurrent requests per second 

    rs = (grequests.get(u) for u in urls)
    grequests.map(rs, exception_handler=exception_handler)
    print("%s request(s) complete to %s" % (c, url))


# start loadgen 
url = os.getenv('SERVER_ADDR') 
if url is None: 
   print("SERVER_ADDR env variable is not defined")
   exit(1)

c_str = os.getenv('REQUESTS_PER_SECOND') 
if c_str is None: 
   print("REQUESTS_PER_SECOND env variable is not defined")
   exit(1)

c = int(c_str)

now = datetime.datetime.now()
print("🚀 Starting loadgen: %s" % now)
schedule.every(1).seconds.do(callserver)

while 1:
   schedule.run_pending()
   time.sleep(1)