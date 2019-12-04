from selenium import webdriver

# setup complete for selenium
# to setup selenium with python in vscode visit https://code.visualstudio.com/docs/python/python-tutorial
# print("you are fucking good!")
path = "F:\github\whatsappbot\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
# print('reached the driver')
name = input("Enter the name or group you want to send a msg")
msg = input("Enter the message")
count = input("Enter the count")

input("Enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
