from bs4 import BeautifulSoup
from dateutil import parser
from ics import Calendar, Event


class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def parse_date(date_str, year):
    return parser.parse(date_str + ", " + year, fuzzy=True)


separators = [" and ", " - ", " to "]


def parse_date_range(date_str, year) -> DateRange:
    for separator in separators:
        if separator in date_str:
            index = date_str.index(separator)

            start = parse_date(date_str[:index], year)
            end = parse_date(date_str[index + len(separator):], year)
            return DateRange(start, end)

    date = parse_date(date_str, year)
    return DateRange(date, date)


def parse_event(title, date_str, year) -> Event:
    event = Event()
    event.name = title

    range = parse_date_range(date_str, year)

    event.begin = range.start
    event.end = range.end
    event.make_all_day()
    return event


calendar = Calendar()

with open('snapshot.html', 'r') as html_file:
    soup = BeautifulSoup(html_file.read(), 'html.parser')

    feeds = soup.find_all(class_="feed")
    for feed in feeds:
        # Here because July 2026 is not within it's feed-blog
        if feed.find("h3") is None:
            month_year = "July, 2026"
        else:
            month_year = feed.find("h3").getText()

        year = month_year[-4:]

        for feed_item in feed.find_all(class_="feed-item"):
            # Here to catch any website mistakes:
            #   - The July 2026 header is in the june blog FOR SOME REASON
            #   - There's an empty feed_item
            if feed_item.find(class_="feed-title") is None or feed_item.find(class_="feed-data") is None:
                continue

            title = feed_item.find(class_="feed-title").getText()
            date = feed_item.find(class_="feed-data").getText()

            event = parse_event(title, date, year)
            calendar.events.add(event)

with open('uvic_events.ics', 'w') as f:
    f.writelines(calendar.serialize_iter())
