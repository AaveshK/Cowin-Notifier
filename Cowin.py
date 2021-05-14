import requests
from win10toast import ToastNotifier
import time
from timeloop import Timeloop
from datetime import timedelta
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d1=d1.replace("/","-")
url= "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="
pin=input("Enter your pin ") 
url=url+pin+"&date="
url=url+d1

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

tl = Timeloop()
hr=ToastNotifier()
age = int(input("What's your age? "))

@tl.job(interval=timedelta(seconds=60)) #Change the value to play with the frequency of updation
def sample_job_every_60s():
     print ("60s job current time : {}".format(time.ctime()))

     response = requests.get(url, headers=headers)
    
     jsonResponse=response.json()
     count = 0
     for i in jsonResponse["centers"]:

          for j in i["sessions"]:
               if int(j["min_age_limit"]) <= age and int(j["available_capacity"])>0:
                    print("\n")
                    print("Date: "+str(j["date"]))
                    print("Slots vacant: "+str(j["available_capacity"]))
                    print("Minimum age limit: "+str(j["min_age_limit"]))
                    print("Vaccine Name: "+j["vaccine"])
                    print("Name: "+i["name"])
                    print("Address: "+i["address"])
                    print("Fee: "+i["fee_type"])
                    print("\n")
                    count += 1
                    if count ==1: hr.show_toast("Vaccine slot alert", "Earliest slot available at "+i["name"]+" on "+str(j["date"]),duration=40)
                         #keep the above line outside (if) to receive all the available slots via notification
               else:
                    continue
     if count>0:
          print("Total options available: "+str(count))
if __name__ == "__main__":
     tl.start(block=True)
