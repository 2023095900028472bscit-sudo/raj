from flask import Flask, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/timezone", methods=["POST"])
def get_time():
    data = request.json
    tz_name = data["timezone"]

    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)

    return {
        "timezone": tz_name,
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(debug=True)
