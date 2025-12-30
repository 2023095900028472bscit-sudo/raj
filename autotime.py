import requests
from datetime import datetime
import pytz

response = requests.get("https://ipapi.co/json/")
data = response.json()

country = data.get("country_name")
timezone_str = data.get("timezone")


timezone = pytz.timezone(timezone_str)
current_time = datetime.now(timezone)

print("Detected Country:", country)
print("Timezone:", timezone_str)
print("Date:", current_time.strftime("%Y-%m-%d"))
print("Time:", current_time.strftime("%H:%M:%S"))
