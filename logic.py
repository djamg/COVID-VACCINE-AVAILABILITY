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
    dicti = {}
    district = 294
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97"}
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district}&date={day}".format(
        district=str(district), day=day)
    # print(url)
    response = requests.get(url, headers=headers)
    response1 = response.json()
    for i in response1["centers"]:
        # print(i["name"])
        for j in i["sessions"]:
            # print(j["available_capacity"])
            # print(j["date"])
            # print(i["name"])
            if j["date"] == day and j["available_capacity"] >= int(availablilty):
                # print(j["min_age_limit"])
                if j["min_age_limit"] == age:
                    dicti[i["center_id"]] = {
                        "hospital_name": i["name"],
                        "vaccine": j["vaccine"],
                        "date": j["date"],
                        "availability": round(int(j["available_capacity"])),
                        "age": j["min_age_limit"],
                        "fee_type": i["fee_type"],
                        "slots": j["slots"]}
    # print(json.dumps(dicti))
    return(json.dumps(dicti))
    # print(response1["centers"]["center_id"])


# search(day=two_day_str, age=45, availablilty=0)
