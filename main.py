import requests
from bs4 import BeautifulSoup
from inquirer import prompt, List 
import os
import subprocess


def search_kinopoisk_ids(query):
    search_url = f'https://www.kinopoisk.ru/index.php?kp_query=%{query}'
    r = requests.get(search_url)
    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.find_all('p', class_='name')
    names = [i.text for i in results]
    ids = [i.a['href'].split('/')[2] for i in results]
    return dict(zip(names, ids))


def search_sources(id):
    source_url = f'https://kinobox.tv/api/players?kinopoisk={id}'
    r = requests.get(source_url)
    return r.json()


def show_iframe(url):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body">
        <iframe src="{url}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
    </body>
    </html>
    """
    html_file = "temp.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    subprocess.Popen(['electron', os.path.abspath(html_file)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print("Enjoy!")
    exit()


def main(query):
    os.system('clear')

    movie_ids = search_kinopoisk_ids(query)
    movie_names = list(movie_ids.keys())

    movie_choice = prompt([
        List('movie', 'Выберите фильм', choices=movie_names)
    ], raise_keyboard_interrupt=True)['movie']

    movie_id = movie_ids[movie_choice]
    sources = search_sources(movie_id)

    source_choices = [f"{source['source']} - {source['translations'][0]['name']}" for source in sources if source['iframeUrl']]

    os.system('clear')

    source_choice = prompt([
        List('source', 'Выберите источник', choices=source_choices)
    ], raise_keyboard_interrupt=True)['source']

    selected_source = next(source for source in sources if f"{source['source']} - {source['translations'][0]['name']}" == source_choice)
    print(f"Выбранный iframeUrl: {selected_source['iframeUrl']}")
    show_iframe(selected_source['iframeUrl'])


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Использование: python kino-cli.py <название фильма>")
    else:
        main(sys.argv[1])