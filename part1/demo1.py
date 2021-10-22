from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\\Users\Giota\PycharmProjects\pythonProject1\pythonSelenium\geckodriver.exe")

driver.get("https://docket-test.herokuapp.com/register")
driver.find_element_by_name("username").send_keys("Giota")
driver.find_element_by_name("email").send_keys("giota.papakonstantinou@gmail.com")
driver.find_element_by_name("password").send_keys("123")
driver.find_element_by_name("password2").send_keys("123")

driver.find_element_by_css_selector("input[value='Register']").click()
ass1= driver.find_element_by_xpath("//html/body/div/div/div/div/form/div").text

assert ass1=='Congratulations, you are now registered'

driver.close()






