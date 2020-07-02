import requests
import os
import bs4

os.makedirs('xkcd', exist_ok=True)
page = input('What issue of xkcd would you like to download? (*all for all comics, *today for today\'s comic): ')
url = 'http://xkcd.com/'


def download_image():
    comic_url = 'http:' + comic[0].get('src')  # page with just the image
    r = requests.get(comic_url)  # switches to that page
    # gets file with directory xkcd/name of comic
    try:
        issue_number = str(int(str(soup.select('a[rel="prev"]')[0].get('href'))[1:-1]) + 1)
    except ValueError:
        issue_number = '1'
    name = os.path.basename(comic_url[:-4] + "_" + issue_number + ".png")
    file = open(os.path.join('xkcd', name), 'wb')
    print("Downloading image %s... " % name)
    # writes to file
    for chunk in r.iter_content(100000):
        file.write(chunk)
    file.close()


if page == '*all':
    url = 'http://xkcd.com/5'
    while not url.endswith('#'):
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        comic = soup.select('#comic img')
        download_image()
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com/' + prev_link.get('href')
else:
    if page == '*today':
        page = ''
    r = requests.get(url + page)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    comic = soup.select('#comic img')

    if not comic:
        print("Comic not found.")
    else:
        download_image()

"""
r = requests.get('https://imgs.xkcd.com/comics/python.png')
# makes file and write the file in bytes to it
with open('comic.png', 'wb') as f:
    f.write(r.content)
"""
