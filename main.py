from flask import Flask, render_template, abort

app = Flask(__name__)

# Приклади записів блогу
posts = [
    {"id": 1, "title": "Подорож до Карпат", "content": "Детальний опис подорожі до Карпат."},
    {"id": 2, "title": "Відпустка на Чорному морі", "content": "Враження від відпочинку на морі."},
    {"id": 3, "title": "Подорож до Львова", "content": "Огляд визначних місць Львова."}
]

# Задача 1: Головна сторінка
@app.route('/')
def home():
    return render_template('home.html')

# Задача 2: Список записів
@app.route('/posts')
def list_posts():
    return render_template('posts.html', posts=posts)

# Задача 3: Деталі запису
@app.route('/posts/<int:id>')
def post_detail(id):
    post = next((post for post in posts if post["id"] == id), None)
    if post is None:
        abort(404)
    return render_template('post_detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
