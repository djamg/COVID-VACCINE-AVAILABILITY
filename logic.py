import requests
import datetime
import json
from datetime import datetime
from datetime import timedelta
import pytz
tz_NY = pytz.timezone('Asia/Kolkata')


date_object = datetime.now(tz_NY)
current_day_str = date_object.strftime("%d-%m-%Y")
# print(current_day_str)

one_day = date_object + timedelta(days=1)
one_day_str = one_day.strftime("%d-%m-%Y")
# print(one_day.strftime("%d-%m-%Y"))

two_day = date_object + timedelta(days=2)
two_day_str = two_day.strftime("%d-%m-%Y")
# print(two_day.strftime("%d-%m-%Y"))


def search(day=current_day_str, age=45, availablilty=1):
    district = 294
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district}&date={day}".format(
        district=str(district), day=day)
    print(url)
    response = requests.get(url).json()
    # response_json = response.json()
    # print(response_json["centers"])
    dictr = []
    print("For age {} and above: ".format(age))
    for i in response["centers"]:
        # print(i["sessions"])
        for j in i["sessions"]:
            # print(j["available_capacity"])
            if j["available_capacity"] >= availablilty:
                if j["min_age_limit"] == age:
                    if j["date"] == day:
                        # print(str(j["available_capacity"]) + " " + j["vaccine"] + " vaccines are available at: " +
                        #       i['name'] + " on " + j['date'] + " between " + str(j['slots']))
                        dictr.append(str(j["available_capacity"]) + " " + j["vaccine"] + " vaccines are available at: " +
                                     i['name'] + " on " + j['date'] +
                                     " between " + str(j['slots']))

    return(dictr)


# search(day=two_day_str, age=45, availablilty=1)


# x = search(day="current_day_str", age=45, availablilty=1)
# print(x)
