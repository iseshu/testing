from seleniumwire import webdriver
import os,time


cors = CORS(app, resources={r"/*": {'Access-Control-Allow-Origin': '*'}})
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')

browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)

newpsw = "hemu.yara"

browser = webdriver.Firefox(executable_path=r"C:\Users\saise\OneDrive\Desktop\driver\geckodriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(3)
browser.find_element_by_name("username").send_keys('_yarra.s.s_')

browser.find_element_by_name("password").send_keys('yarra.s')

browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

time.sleep(5)

browser.get('https://www.instagram.com/accounts/password/change/')

time.sleep(3)

browser.find_element_by_name('cppOldPassword').send_keys('yarra.s')

browser.find_element_by_name("cppNewPassword").send_keys(newpsw)

browser.find_element_by_name("cppConfirmPassword").send_keys(newpsw)

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[4]/div/div/button').click()

print(newpsw)
