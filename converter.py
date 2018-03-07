from datetime import datetime
from us_timezones import us_time
import pytz

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("Enter date here: (set date as shown --> MM/DD/YYYY HH:MM format)")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".format(date_input))
    else:
        # Enter Your Local Timezone Below
        local_date = pytz.timezone('US/Eastern').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []
        for timezone in us_time:
            output.append(utc_date.astimezone(timezone))
        for date_time in output:
            print(date_time.strftime(fmt))
        break
