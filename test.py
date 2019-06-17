from itertools import tee, islice
from collections import Counter
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Xenia/Downloads/chromedriver.exe")
data_list = []
loop = 1
fin_data = str
while loop <= 100:
    driver.get("https://www.random.org/integers/")
    arr_length = driver.find_element_by_name("num")
    arr_length.clear()
    arr_length.send_keys("10000")

    dia_min = driver.find_element_by_name("min")
    dia_min.clear()
    dia_min.send_keys("0")

    dia_max = driver.find_element_by_name("max")
    dia_max.clear()
    dia_max.send_keys("1")

    cols = driver.find_element_by_name("col")
    cols.clear()
    cols.send_keys("10000")

    driver.find_element_by_css_selector("#invisible > form > p:nth-child(10) > input[type=submit]:nth-child(1)").click()

    data = driver.find_element_by_xpath("//*[@id=\"invisible\"]/pre").text
    fin_data = str(data)
    fin_data.replace(' ', '')

    for i in fin_data:
        if i != ' ':
            data_list.append(i)

    loop += 1


def ngrams (list, n):
    tlist = list
    while True:
        a, b = tee(tlist)
        l = tuple(islice(a, n))
        if len(l) == n:
            yield l
            next(b)
            tlist = b
        else:
            break


print('LIST LENGTH: ', len(data_list))
print('0 1 FREQ: ',Counter(data_list))
print('0 PERCENTAGE: ', data_list.count('0')*100/len(data_list), '%')
print('1 PERCENTAGE ',  data_list.count('1')*100/len(data_list), '%')
c = Counter(ngrams(data_list, 2))
print('BIGRAMMS FREQ: ', Counter(ngrams(data_list, 2)))
print('BIGRAMMS PERCENTAGE: ', [(i, c[i]/len(data_list)*100.0) for i in c])
print('THREEGRAMMS FREQ: ', Counter(ngrams(data_list, 3)))
print('THREERAMMS PERCENTAGE: ', [(i, c[i]/len(data_list)*100.0) for i in c])


driver.close()