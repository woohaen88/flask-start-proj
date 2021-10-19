from flask import Blueprint, render_template

from proj.forms.autho_form import LoginForm, RegisterForm

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        password = form.data.get('password')
        return f'{user_id}, {password}'

    else:
        # Error
        pass

    return render_template(f'{NAME}/login.html', form=form)

@bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')
        return f'{user_id},{user_name}, {password}, {repassword}'

    else:
        pass

    return render_template(f'{NAME}/register.html', form=form)

@bp.route('/auth/logout')
def logout():
    return 'logout'