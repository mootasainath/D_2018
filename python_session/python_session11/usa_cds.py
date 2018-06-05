from urllib.request import urlopen
from xml.etree.ElementTree import XML

def get_data(url):
	d = urlopen(url)
	data = d.read()

	return data

def print_usa_cds(url):
	data = get_data(url)
	dx = XML(data)

	for cd in dx.findall("./CD"):
		if cd.find("./COUNTRY").text == "USA":
			print(cd.find("./TITLE").text)

if __name__ == "__main__":
	print_usa_cds("https://www.w3schools.com/js/cd_catalog.xml")
