#taskkill /f /im python.exe

from flask import Flask, render_template, flash, redirect, session, url_for, request, abort
from forms import LoginForm

from MyConfig import Config

app = Flask(__name__)
app.config.from_object(Config)
users_passwords = {'zenya':'12345','sasha':'80','lesha':'321','vitya':'Hds_123Ldasf_212_google_zxc','arseniy':'000','kostya':'password','afanasiy':'666',
'evdakim':'zxc','anatolyi':'dead_inside','ded_inside':'16','viktor':'124214','vlad':'12'}
def print_inventory(dct):
    print("Users:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))
@app.route('/kuku')
def hi():  # put application's code here
    return 'sdfsdf!'


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash(f"Зашел пользователь под логином {form.username.data}, запомнить = {form.remember_me.data}")
        return redirect('/index')

    return render_template('login.html', title='Авторизация пользователя', form=form)

@app.route('/login2', methods=['POST', 'GET'])
def login2():
    if 'userlogged' in session:
        return redirect(url_for('profile', username=session['userlogged']))
    elif request.method == 'POST' and request.form['username'] in users_passwords and request.form['psw'] == users_passwords[request.form['username']]:
        session['userlogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userlogged']))


    return render_template('login_2var.html', title='Авторизация пользователя')

@app.route('/users')
def users():
    user = users_passwords
    password = 0
    return render_template('users.html', users_passwords = users_passwords)


@app.route('/new_user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        users_passwords[request.form['username']] = request.form['psw']

    return render_template('new_user.html', title='Регистрация пользователя')

@app.route('/profile/<username>')
def profile(username):
    if 'userlogged' not in session or session['userlogged'] != username:
        abort(401)
    return f"<h1> Пользователь {username}</h1>"

@app.route('/')
@app.route('/index')
def index():  # put application's code here
    car = {'name': ('bugatty',
                    'https://libertycity.ru/uploads/download/gta5_bugatti/fulls/j4q9k776k31rt5p2jnd2823s63/15043684584016_f61541-1.jpg')}

    return render_template('index.html', name=car['name'][0], foto=car['name'][1], title='1')


@app.route('/petya/')
def petya():  # put application's code here
    return ''' <h2> Александр Твардовский

Василий Теркин. Сборник

Лирика

РОДНОЕ

<br>Дорог израненные спины, </br>
<br>О дальних шумных городах. </br>
    </h2> '''


# @app.route('/user/<username>')
# def user_profile(username):  # put application's code here
#     return f"<h1>Здраствуй дорогой пользователь {username}</h1>"
#
#
# @app.route('/user/<int:post_id>')
# def show_post(post_id):  # put application's code here
#     return f"<h1>Горячая и свежая новость № {post_id}</h1>"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена')


if __name__ == '__main__':
    app.run(debug=True)
