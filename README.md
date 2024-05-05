<h2 align="center">
Консольная утилита для просмотра фильмов.
</h2>
<h4 align='center'>
Эта программа использует <a href="https://www.kinopoisk.ru/">кинопоиск</a> для поиска фильмов и <a href = "https://kinobox.tv/">kinobox</a> для поиска плеера.
</h4>

## Демонстрация
[2024-05-06-01-54-41-_online-video-cutter.com_.webm](https://github.com/Forwall100/kino-cli/assets/78537089/38d2f33a-fc09-4ae6-8455-26c31f0fbaaa)


## Устанока (arch linux)
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
sudo pacman -S electron
```
4. Добавьте строку в ~/.bashrc
```bash
alias kino-cli='<путь к .venv/bin/python3> <путь к скрипту main.py>'
```
5. Примените изменения в bashrc
```bash
source .bashrc
```

## Использование
Запуск плеера в electron
```bash
kino-cli <название фильма>
```
Запуск плеера в браузере
```bash
kino-cli --browser <название фильма> 
```

## Лицензия
Программа работает на основе плеера [Kinobox.tv](https://kinobox.tv/), и предоставляется исключительно в ознакомительных целях!
**_Пиратство - плохо!_**

MIT _([LICENSE](https://github.com/Forwall100/kino-cli/blob/main/LICENSE) файл)_
