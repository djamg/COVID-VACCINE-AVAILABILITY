import requests
import datetime
import json

date_object = datetime.date.today()
date_str = date_object.strftime("%d-%m-%Y")
print(date_str)

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
            print(str(j["available_capacity"]) + " vaccines are available at: " +
                  i['name'] + " on " + j['date'] + " between " + str(j['slots']))
            # print("Vaccine is available at: " +
            #       i['name'] + ", on: " + j['date'] + " at: " + j['slots'])
