import datetime

timezone = +7 #utc+7 (+7) // utc-7 (-7)
current_utc = datetime.datetime.utcnow()
current_timezone = current_utc + datetime.timedelta(hours=timezone)
print(current_timezone)
