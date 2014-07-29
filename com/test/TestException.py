import csv, os
import time

filepath = os.path.join('C:/Users/mohammad.ali/workspace-trunk/PyDevProject/test.csv')
reader = csv.reader(open(filepath))

for NAME,Id,No,Dept,EndDate in reader:
    if NAME!='NAME':
        billing_time = str(time.strptime(EndDate, '%m/%d/%Y'))
        print(billing_time)
        print("insert into msg_alert_subscription (NAME,Id,No,Dept,EndDate) values('"+NAME+"',"+Id+","+No+",'"+Dept+"','"+billing_time+"');")