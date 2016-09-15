from datetime import datetime
from app import app


@app.template_filter('timestamp_to_date')
def timestamp_to_data(timestamp):
    date = datetime.fromtimestamp(int(timestamp))

    return date.strftime("%m/%d/%Y")

@app.template_filter('timestamp_to_time')
def timestamp_to_data(timestamp):
    date = datetime.fromtimestamp(int(timestamp))

    return date.strftime("%I:%M:%S %p")