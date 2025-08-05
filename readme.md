# Uvic Important Academic Dates Parser

This is a hyper-specific program that parses all the dates from https://www.uvic.ca/calendar/dates/ (website snapshot required) into an ics file that can be imported into any calendar application. 

## Project Status

I only intend to use this project rarely, and it works fine, so I don't intend to do any work on it unless I need to for personal use. 

## Installation / Running

To generate the ics file, you can either use the existing snapshot.html (which is accurate as of August 5th, 2025 💀) file, or you can get the latest information by getting your own snapshot.

To grab the current site information, go to https://www.uvic.ca/calendar/dates/, right click then click `Save Page As`. Rename the file to exactly `snapshot.html` then replace the existing file in the repository.

Finally, run main.py to generate the ics. This will replace the existing `uvic_events.ics` in the repo

## Requirements

The project requires 3 python libraries:
- [ics.py](https://icspy.readthedocs.io/en/stable/#)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [dateutil](https://pypi.org/project/python-dateutil/)