import requests
import sys
from bs4 import BeautifulSoup
from inquirer import prompt, List
import os
import tempfile
import subprocess
import webbrowser

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

def show_iframe(url, use_browser=False):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {{
    margin: 0;
    padding: 0;
    background-color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }}
    .iframe-container {{
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    }}
    iframe {{
    width: 80vw;
    height: 80vh;
    border: none;
    }}
    </style>
    </head>
    <body>
    <div class="iframe-container">
    <iframe src="{url}" frameborder="0" allowfullscreen></iframe>
    </div>
    </body>
    </html>
    """

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".html") as temp_file:
        temp_filename = temp_file.name
        temp_file.write(html_content)

    if use_browser:
        webbrowser.open(f"file://{temp_filename}", new=2)
    else:
        subprocess.Popen(['electron', temp_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    print("Enjoy!")
    exit()

def main(query, use_browser=False):
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

    show_iframe(selected_source['iframeUrl'], use_browser)

if __name__ == '__main__':
    use_browser = '--browser' in sys.argv
    if len(sys.argv) < 2 or (len(sys.argv) == 2 and '--browser' in sys.argv):

        print("""
Использование: python kino-cli.py <название фильма> 

Параметры:
--browser: открывать плеер в браузере
              """)
    else:
        query = sys.argv[1] if not use_browser else sys.argv[2]
        main(query, use_browser)