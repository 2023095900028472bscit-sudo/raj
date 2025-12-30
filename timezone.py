import requests
from datetime import datetime
import pytz

# Get timezone from IP
data = requests.get("https://ipapi.co/json/").json()
timezone = data["timezone"]

tz = pytz.timezone(timezone)
now = datetime.now(tz)

print("Timezone:", timezone)
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
