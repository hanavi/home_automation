#!/usr/bin/env python3
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


path="/usr/local/bin/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(executable_path=path, chrome_options=options)
vivent_url = "https://www.vivintsky.com/app/#/account"
driver.get(vivent_url)

sleep(5)

email_css = '#login-form > div:nth-child(1) > input[type="email"]'
email_addr = "hanavi@gmail.com"
passwd_css = '#login-form > div:nth-child(2) > input[type="password"]'
passwd = "xxxx"


s = driver.find_element_by_css_selector(email_css)
s.send_keys(email_addr)

s = driver.find_element_by_css_selector(passwd_css)
s.send_keys(passwd)

s = driver.find_element_by_css_selector('#login-form > button')
s.click()

mom_home = ('#shared-homes > viv-shared-homes-card > md-card > md-card-content'
            '> div.shared-homes-container.layout-wrap.layout-row > div:nth-chi'
            'ld(2) > md-card > md-card-content > div.layout-align-space-around'
            '-start.layout-column.flex > div.ac-shared-home__text.ac-shared-ho'
            'me__links.layout-align-space-around-center.layout-row > a:nth-chi'
            'ld(1)')

sleep(5)

s = driver.find_element_by_css_selector(mom_home)
s.click()


d1 = ("#container > div > div > section > div > div > div > div > div >"
      "div.viv-grid__column.ng-scope.viv-grid__security-column >"
      "section.ng-scope.viv-grid__security > div > div > div >"
      "div.viv-security__body > div.viv-security__control >"
      "div.viv-security-locks > div.ng-scope.column.right > div >"
      "div.viv-slider.ng-isolate-scope.binary.slider-off >"
      "div.active-circle.grab-point")


d2 = ("#container > div > div > section > div > div > div > div > div >"
      "div.viv-grid__column.ng-scope.viv-grid__security-column >"
      "section.ng-scope.viv-grid__security > div > div > div >"
      "div.viv-security__body > div.viv-security__control >"
      "div.viv-security-locks > div.ng-scope.column.right > div >"
      "div.viv-slider.ng-isolate-scope.binary.slider-off >"
      "div.icon-block.qa-slider-32 >"
      "i.label.on.viv-icon-gdo-closed.qa-slider-32-closed")

sleep(5)

s1 = driver.find_element_by_css_selector(d1)
s2 = driver.find_element_by_css_selector(d2)

ActionChains(driver).drag_and_drop(s1, s2).perform()
sleep(10)

driver.close()
