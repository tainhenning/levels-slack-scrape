from selenium import webdriver
import json
import constants

def main():
    with open(constants.JSON_PATH) as f:
        fyi_links = json.load(f)
    driver = webdriver.Chrome()
    driver.get(fyi_links[constants.NETFLIX_SALARY_LINK])
    recent_salary = driver.find_element_by_xpath(fyi_links[constants.RECENT_SALARY_XPATH])
    recent_yoe = driver.find_element_by_xpath(fyi_links[constants.RECENT_YOE_XPATH])
    recent_level_name = driver.find_element_by_xpath(fyi_links[constants.RECENT_LEVEL_NAME_XPATH])

    print(recent_level_name.text, recent_salary.text, recent_yoe.text)

if __name__ == '__main__':
    main()