# Cowin-Notifier
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAaveshK%2FCowin-Notifier&count_bg=%2324A620&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=false)](https://hits.seeyoufarm.com)
## What does it do?
### Informs you about all the vaccination slots available for you within a week
## Platform supported
>Windows
## Installation
### Clone the repository
`git clone https://github.com/AaveshK/Cowin-Notifier.git`
### Install the required libraries
`pip install -r requirements.txt`
## Working
### Run the Cowin.py file
`python cowin.py`
1. Enter your pincode
2. Enter your age
### That's it. The script will now keep you updated every minute.
## Getting notifications
### Make sure that the Focus assist is off and not priority only/alarms only
![alt text](https://github.com/AaveshK/Cowin-Notifier/blob/main/FocusAssist.png?raw=true)
### When any vacant slot is found
![alt text](https://github.com/AaveshK/Cowin-Notifier/blob/main/Cowin.png?raw=true)
### If there are no slots available, there will not be any notification and the terminal will look similar to this
![alt text](https://github.com/AaveshK/Cowin-Notifier/blob/main/Unavailable.JPG?raw=true)
## Modifications
### 1. The updation time can be changed by changing 
***60*** in
`@tl.job(interval=timedelta(seconds=60))`
#### By default, the updation occurs every 60 seconds
### 2. The duration of the notification can be increased/decreased by changing 
***40*** in 
`if count ==1: hr.show_toast("Vaccine slot alert", "Earliest slot available at "+i["name"]+" on "+str(j["date"]),duration=40)`
#### The default time is 40 seconds

## Known Issues
- [windows python service error: (-2147467259, 'Shell_NotifyIcon', 'Unspecified error')  ](https://github.com/jithurjacob/Windows-10-Toast-Notifications/issues/18)  
This is rare, and restarting the system fixes it for me. 
