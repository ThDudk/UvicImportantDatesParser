# Uvic Important Academic Dates Parser

Parses all the academic important dates from https://www.uvic.ca/calendar/dates/ (website snapshot required) into an ics file that can then be imported into any calendar application. 

## Installation / Running

To generate the ics file, you can either use the existing snapshot.html (which is accurate as of August 5th, 2025 💀) file, or you can get the latest information by getting your own snapshot.

To grab the current site information, go to https://www.uvic.ca/calendar/dates/, right click then click `Save Page As`. Rename the file to exactly `snapshot.html` then replace the existing file in the repository.

Finally, run main.py to generate the ics. This will replace the existing `uvic_events.ics` in the repo

## Built With
- [ics.py](https://icspy.readthedocs.io/en/stable/#)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [dateutil](https://pypi.org/project/python-dateutil/)

## Project Status

I don't intend to do any more work on this project. I can't guarentee it will continue to work in the future and I won't fix any bugs or issues unless I personally intend to use the project again.  
