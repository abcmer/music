from jazz_radio_scraper import WCDBDailyPlaylist

def test_date_parser():
	date_str = WCDBDailyPlaylist.parse_date_string('Tuesday - February 09, 2021')
	assert date_str == '2021-02-09'

def test_scraper():
	dates = ["2021-02-09", "2021-02-10", "2021-02-11", "2021-02-12", "2021-02-13"]
	for date in dates:
		playlist = WCDBDailyPlaylist(date)		