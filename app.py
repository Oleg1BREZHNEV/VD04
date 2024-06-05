
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    days_of_week = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    months_of_year = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября",
                      "Ноября", "Декабря"]

    day_of_week = days_of_week[now.weekday()]
    day = now.day
    month = months_of_year[now.month - 1]
    year = now.year
    time = now.strftime("%H:%M:%S")

    current_time = f"{day_of_week}, {day} {month} {year} года {time}"
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)

