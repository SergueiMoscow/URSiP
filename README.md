# Тестовое задание для URSiP
Перед запуском необходимо:
+ установить зависимости: <code>pip install -r requirements.txt</code> 


+ создать БД, запустив <code>db/create_db</code>


+ прописать (в <code>main.py</code>, константа <code>FILENAME</code>) имя входящего xls файла.
 

+ Файл запуска - <code>main.py</code>


+ Программа проверяет, были ли подгружены данные с указанного файла. Если были, то она их повторно не подгружает.
В конце выводит в консоль статистику сгруппированную по дате и типу (liq, oil).
