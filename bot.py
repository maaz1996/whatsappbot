from selenium import webdriver
# setup complete for selenium
# to setup selenium with python in vscode visit https://code.visualstudio.com/docs/python/python-tutorial
#print("you are fucking good!")

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print('reached the driver')
