import random 
import time 

def Date(start_date, end_date):
    random_generator = random.random()
    Date_format = "%m/%d/%y"
    start_time = time.mktime(time.strptime(start_date, Date_format))
    end_time = time.mktime(time.strptime(end_date, Date_format))
    random_time = start_time + random_generator * (end_time - start_time)
    random_date = time.strftime(Date_format, time.localtime(random_time))
    return random_date
print(Date("4/3/22", "6/8/25")) 




