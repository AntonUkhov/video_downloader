import requests
from bs4 import BeautifulSoup

# присваевыем переменной значение
# и делаем запрос
html_url = "https://www.vidsplay.com/"
html_response = requests.get(html_url)


# при помощи BeautifulSoup преобразуем данные
soup = BeautifulSoup(html_response.text, 'html.parser')

# сохраняем веб страницу
with open('test.html', 'w', encoding="utf-8") as f:
    f.write(html_response.text)

# с помощью цикла находим все теги
# сохраняем видео с именем(разбив его по слешу и оставив последнее значение по индексу)
for mp4 in soup.find_all('video'):
    mp4 = mp4['src']
    print("Downloading {}".format(mp4))
    with open(mp4.split("/")[-1].strip(), "wb") as f_out:
        f_out.write(requests.get(mp4).content)
