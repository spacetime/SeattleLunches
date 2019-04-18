import requests
import datetime
import json

date_today=datetime.datetime.now()
date_tomorrow=date_today + datetime.timedelta(days=1)
request = 'https://www.seattlefoodtruck.com/api/events'

payload = {'page' : 1,
           'page_size' : 30,
           'start_date' : date_today.strftime("%m-%d-%y"),
           'end_date' : date_tomorrow.strftime("%m-%d-%y"),
           'for_locations' : 38, #Westlake=38
           'with_active_trucks' : 'true',
           'include_bookings' : 'true',
           'with_booking_status' : 'approved' }
#print(request)
try:
    r = requests.get(request, params=payload, timeout=50, headers={'user-agent': 'fetch_lunch/0.0.1'})
    #print(r.text)
    response_json = json.loads(r.text)
    for event in response_json['events']:
        print("\nEvent: ", str(event['id']))
        for booking in event["bookings"]:
            print("    " + booking['truck']['name'])
except:
    print('No response, try again')

