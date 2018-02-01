import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import Testing
import os
import urllib.request
import requests

import json
import sys
import time, os

MAX_SUBS = 1000000
MAX_CF_CONTEST_ID = 600
MAGIC_START_POINT = 17000

handle = 'tacklemore'

#SOURCE_CODE_BEGIN = '<pre class="prettyprint program-source" style="padding: 0.5em;">'
SOURCE_CODE_BEGIN = 'prettyprint lang-'.encode()
SUBMISSION_URL = 'http://codeforces.com/contest/{ContestId}/submission/{SubmissionId}'
USER_INFO_URL = 'http://codeforces.com/api/user.status?handle={handle}&from=1&count={count}'

EXT = {'C++': 'cpp', 'C': 'c', 'Java': 'java', 'Python': 'py', 'Delphi': 'dpr', 'FPC': 'pas', 'C#': 'cs'}
EXT_keys = EXT.keys()

langs = {'cpp', 'c', 'java','py', 'dpr', 'pas', 'cs'}

replacer = {'&quot;': '\"', '&gt;': '>', '&lt;': '<', '&amp;': '&', "&apos;": "'"}
keys = replacer.keys()


def get_ext(comp_lang):
    if 'C++' in comp_lang:
        return 'cpp'
    for key in EXT_keys:
        if key in comp_lang:
            return EXT[key]
    return ""


def parse(source_code):
    for key in keys:
        source_code = source_code.replace(key.encode(), replacer[key].encode())
    return source_code


if not os.path.exists(handle):
    os.makedirs(handle)





def login():
    # get the path of ChromeDriverServer
    dir = os.path.dirname(__file__)
    #driver = webdriver.PhantomJS(r"C:\Users\kross\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    chrome_driver_path = dir + "\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)

    #driver.implicitly_wait(30)
    driver.maximize_window()

    URL = 'http://codeforces.com/enter?back=%2F'
    # navigate to the application home page
    driver.get(URL)
    #print('fsd')
    # get the search textbox
    search_field = driver.find_element_by_id("handle")
    search_field.send_keys("sam_267")
    search_field = driver.find_element_by_id("password")
    search_field.send_keys("9582501267")
    x=search_field.submit()

    driver.implicitly_wait(50)

    return driver

def startHacking(max_pages):
    page = 1
    driver = login()
    while page <= max_pages:
        url = "http://codeforces.com/contest/903/status/A/page/" + str(page) + "?order=BY_ARRIVED_DESC"
        #url = "http://codeforces.com/contest/915/status/A/page/" + str(page) + "?order=BY_ARRIVED_DESC"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")

        view_source = soup.findAll('a', {'class': 'view-source'})
        verdict = soup.findAll('span', {'class': 'verdict-accepted'})

        i = 0
        for verd in verdict:
            if  verd.text == "Accepted" :
            #if i<1:
                code_url = "http://codeforces.com" + view_source[i].get('href')
                con_id = code_url[30:33]
                sub_id = code_url[45:53]
                #33192843
                submission_info = urllib.request.urlopen(SUBMISSION_URL.format(ContestId=int(con_id), SubmissionId=sub_id)).read()
                # print(submission_info)

                start_pos = submission_info.find(SOURCE_CODE_BEGIN, MAGIC_START_POINT) + len(SOURCE_CODE_BEGIN)
                end_pos = submission_info.find("</pre>".encode('utf-8'), start_pos)
                result = parse(submission_info[start_pos:end_pos]).replace('\r'.encode('utf-8'), ''.encode('utf-8'))
                # ext = get_ext(comp_lang)
                con_id = 915
                con = str(con_id)
                new_directory = handle + '/' + con
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)
                file = open(new_directory + '/' + 'cd' + '[ ' + 'hey' + ' ]' + '.' + 'cpp', 'w', encoding='utf-8')
                file.write(result.decode('utf-8'))
                file.close()
                plain_text = (result.decode('utf-8'))

                fl = 0
                text = ''
                for link in plain_text:
                    if link == '>':
                        fl = 1
                    if fl == 1:
                        text = text + link

                text=text[1:]
                custom_code=text
                #code_url = "http://codeforces.com/contest/915/submission/34174730"

                code = requests.get(code_url)
                plain = code.text
                code_soup = BeautifulSoup(plain, "lxml")
                rows = code_soup.findAll('td')
                lang = rows[3].text[6:-6]
                #print(lang)
                new_directory = handle + '/' + con
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)
                file = open(new_directory + '/' + 'cd' + '[ ' + 'hey' + ' ]' + '.' + 'cpp', 'w', encoding='utf-8')
                file.write(result.decode('utf-8'))
                file.close()
                Testing.custom_invoc(sub_id,custom_code, lang, driver)
            i+=1



        page += 1


startHacking(1)
