<h2 align="center">
Консольная утилита для просмотра фильмов.
</h2>
<h4 align='center'>
Эта программа использует <a href="https://www.kinopoisk.ru/">кинопоиск</a> для поиска фильмов и <a href = "https://kinobox.tv/">kinobox</a> для поиска плеера.
</h4>

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
```bash
kino-cli <название фильма>
```

## Лицензия
Программа работает на основе плеера [Kinobox.tv](https://kinobox.tv/), и предоставляется исключительно в ознакомительных целях!
**_Пиратство - плохо!_**

MIT _([LICENSE](https://github.com/Forwall100/kino-cli/blob/main/LICENSE) файл)_
