import requests
import bs4
from urllib.request import urlopen as uReq
# Creating URL

phone = input('Enter phone name: ')
phone = phone.replace(' ', '%20')
phone = phone.replace('.', '')
res = requests.get('https://www.google.com/search?q=91%20mobiles%20' + phone)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElements = soup.select('.r a')
x = linkElements[1].get('href')
n = x.index('&sa=')
x = x[7:n]
my_url = x


print("\n                     Loading.....                  \n")

try:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = bs4.BeautifulSoup(page_html, "html.parser")

    # Finding Spec Box
    containers = page_soup.findAll("div", {"class": "spec_box"})
    # print(len(containers))

    container = containers[0]

    f = open('file.txt', 'a')
    # headers = "Product Name, Price, Ratings\n"
    # f.write(headers)

    for container in containers:
        # print(soup.prettify(container))

        # Finding Tr
        trs = (container.findAll("tr"))
        # print(len(trs))

        tr = trs[0]

        for tr in trs:
            # print(soup.prettify(trs[0]))

            # Finding Title
            title = tr.findAll("td", {"class": "spec_ttle"})
            if title:
                new_title = title[0].text
                print(new_title + " :")
                f.write(new_title + ":\n")

            result = tr.findAll("td", {"class": "spec_des"})
            # my_result = result[0].text
            # result = result.replace(" ", " ")
            # new_result = new_result.replace("\n", "")
            # result = result.replace("CompareSize", "")
            if result:
                if 'All Phones' in result[0].text:
                    continue
                new_result = result[0].text
                new_result = new_result.replace("     ", " ")
                new_result = new_result.replace("\n", "")
                final_result = new_result
                print(final_result)
                f.write(final_result + "\n")
    f.write("\n-------------------------------------------------------\n\n")
    f.close()
    fail = 'no'
except:
    print("Sorry try again!")
