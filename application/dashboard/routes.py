from flask import render_template

from . import dashboard_blueprint


@dashboard_blueprint.route('/')
def index():
  return render_template('index.html')


@dashboard_blueprint.route('/sad')
def unknown():
  return render_template('404.html')
