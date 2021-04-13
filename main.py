from meet import enter_meet
import schedule,time

dash = "-" * 50
# I take your Meeting details here 
url=input("Enter gmeet url:")
meet_time=input("Enter meet time in 24hr format, like 13:30 for 1:30pm,09:30 for 9:30am:")
meet_time = str(meet_time)

#I make sure you have entered the correct time
print(dash)
print("Everyday schedule set at {}".format(meet_time))
print(dash)

#I take your prefered Browser wherein you have logged-in with your google account
def_browser=input("Enter default browser: i.e...Chrome,Microsoft Edge,Firefox:")

#I schedule your job everyday at the same time and run it
schedule.every(1).day.at(meet_time).do(enter_meet,def_browser,url)

while True:
    schedule.run_pending()
    time.sleep(1)