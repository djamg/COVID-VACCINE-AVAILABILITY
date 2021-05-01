import requests
import datetime
import json
from datetime import timedelta

date_object = datetime.date.today()
date_str = date_object.strftime("%d-%m-%Y")
# print(date_str)

one_day = date_object + timedelta(days=1)
# print(one_day.strftime("%d-%m-%Y"))

two_day = date_object + timedelta(days=2)
# print(two_day.strftime("%d-%m-%Y"))

district = 294
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
    str(district), date_str)

response = requests.request("GET", url)
response_json = response.json()
# print(response_json["centers"])

for i in response_json["centers"]:
    # print(i["sessions"])
    for j in i["sessions"]:
        # print(j["available_capacity"])
        if j["available_capacity"] > 0:
            if j["date"] == one_day.strftime("%d-%m-%Y"):
                print(str(j["available_capacity"]) + " " + j["vaccine"] + " vaccines are available at: " +
                      i['name'] + " on " + j['date'] + " between " + str(j['slots']))
