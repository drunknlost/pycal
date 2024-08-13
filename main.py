import requests
from ics import Calendar

url = "https://calendar.google.com/calendar/ical/ht3jlfaac5lfd6263ulfh4tql8%40group.calendar.google.com/public/basic.ics"



response = requests.get(url)
response.raise_for_status()  # Check for request errors

calendar = Calendar(response.text)

for event in calendar.events:
    print(f"Event: {event.name}")
    print(f"Start: {event.begin}")
    print(f"End: {event.end}")
    print(f"Logs: {event.description}")
    print("-" * 20)
