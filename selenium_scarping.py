
import time
from selenium import webdriver
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set the path to the ChromeDriver executable
chromedriver_path = "/usr/bin/chromedriver"

# Create a service object with the executable path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Create the WebDriver with the service and desired capabilities
driver = webdriver.Chrome(service=chrome_service)

# Now you can access the capabilities like this:
browser_name = driver.capabilities['browserName']

url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'

driver.get(url)

while(True):
	now = datetime.now()
	
	# this is just to get the time at the time of
	# web scraping
	current_time = now.strftime("%H:%M:%S")
	print(f'At time : {current_time} IST')
	c = 1

	for x in range(3, 9):
		curr_path = ''
		
		# Exception handling to handle unexpected changes
		# in the structure of the website
		try:
			curr_path = f'/html/body/c-wiz/div/div[2]/div[2]/\
			div/main/c-wiz/div[1]/div[{x}]/div/div/article/h3/a'
			title = driver.find_element_by_xpath(curr_path)
			print(title)
		except:
			continue
		print(f"Heading {c}: ")
		c += 1
		print(title.text)
		
	# to stop the running of code for 10 mins
	time.sleep(600)

