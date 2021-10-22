

from selenium import webdriver

drivers=webdriver.Firefox(executable_path="C:\\Users\Giota\PycharmProjects\pythonProject1\pythonSelenium\geckodriver.exe")

drivers.get("https://docket-test.herokuapp.com/login")

drivers.find_element_by_css_selector("input[name='username']").send_keys("Giota")
drivers.find_element_by_css_selector("input[name='password']").send_keys("123")
drivers.find_element_by_css_selector("input[name='remember_me']").click()

drivers.find_element_by_name(name="submit").click()


ass1= drivers.find_element_by_xpath("//html/body/div/div/div/div/strong/h1").text

assert ass1=='Hello Giota'

drivers.close()







