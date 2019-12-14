from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import user_form
user = Blueprint('user', __name__,
                        template_folder='templates')

@user.route('/register', methods=['GET', 'POST'])
def register():
    login_form = user_form.RegisterForm()
    try:
        return render_template('user/register.html')
    except TemplateNotFound:
        abort(404)