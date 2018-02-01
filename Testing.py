from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time,os

language={'PascalABC.NET':'PascalABC.NET2','GNU C++':'GNU G++ 5.1.0','GNU C++14':'GNU G++14 6.4.0','GNU C++11':'GNU G++11 5.1.0','GNU C11':'GNU GCC C11 5.1.0','Java 8':'Java 1.8.0_131','GNU C':'GNU GCC 5.1.0','Python 2':'Python 2.7','Python 3':'Python 3.6','MS C++':'Microsoft Visual C++ 2010','JavaScript':'JavaScript V8 4.8.0','PyPy 3':'PyPy 3.5.3 (5.10.0)','PyPy 2':'PyPy 2.7.13 (5.9.0)','GNU C++17 Diagnostics':'GNU C++17 Diagnostics (DrMemory)','Clang++17 Diagnostics':'Clang++17 Diagnostics'}

def custom_invoc(id,custom_code, lang, driver):

    #driver = webdriver.Chrome(executable_path=r"G:\chromedriver_win32\chromedriver.exe")
    testing_url = "http://codeforces.com/contest/915/customtest"

    input = "2 6 5"
    desired_output = "YES\nNO"

    driver.get(testing_url)

    btn = driver.find_elements_by_name("submit")[0]
    select = Select(driver.find_element_by_name('programTypeId'))

    # select by visible text
    select.select_by_visible_text('Haskell GHC 7.8.3')

    # driver.find_elements_by_id("toggleEditorCheckbox")[0].click()

    driver.implicitly_wait(100)

    #txt = driver.find_elements_by_class_name("ace_text-input")[0]
    #txt.clear()
    #txt.send_keys(custom_code)
    driver.find_element_by_name("inputFile").send_keys(os.getcwd() + "/mario.py")
    test = driver.find_elements_by_name("input")[0]
    test.send_keys(input)

    driver.implicitly_wait(100)
    #select.select_by_visible_text(lang)
    print(language[lang])
    select.select_by_visible_text(language[lang])
    #print('fsa')
    driver.implicitly_wait(100)

    # driver.find_elements_by_id("toggleEditorCheckbox")[0].click()
    btn.submit()

    driver.implicitly_wait(1000)

    time.sleep(5)
    #op = driver.find_elements_by_name("output")[0]
    # get the textarea element by tag name
    textarea = driver.find_element_by_name('output')
    time.sleep(5)
    output='Runn'
    while output[:4]=='Runn':
        try:
            # print the attribute of the textarea
            output = textarea.get_attribute('value')
            o = output.replace("\n", " ")
            #print(output)
            #print(o)
        except:
            print('No output')


    i = 0
    b = 1
    for s in desired_output:
        if s != output[i]:
            b = 0
            break
        i+=1
    if(b):
        print("Don't Hack")
    else:
        print("Hack id:!! " +id)

    #print(lang)
    #print(textarea.get_attribute('rows'))
    #print(textarea.get_attribute('cols'))

    #output = driver.find_elements_by_name("output")[0]
    #print(output.getText())
    #print(repr(op.text))


    driver.implicitly_wait(1000)
