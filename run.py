"""Automation script.

Usage:
  run.py dry
  run.py back
  run.py front
  run.py pop
  run.py pop --dev
  run.py djapp <app>
  run.py -h | --help

Arguments:
  args          show the arguments
  back          run the django server
  front         run the Vue.js server
  pop           populate the django database

Options:
  -h --help     Show this screen
  --dev         Populate the database for development

"""

import os
import sys
import subprocess

from docopt import docopt
import colorama


PIPENV = "pipenv run"
MANAGE = f"{PIPENV} python manage.py"


def activate_colors_on_windows():
    """Colors in the shell."""
    colorama.init()
    os.environ['ANSICON'] = 'on'


def back():
    """Run the Django server."""
    subprocess.call(f"{MANAGE} runserver", shell=True)


def pop(dev=False):
    """Populate the database."""
    subprocess.call(f"{MANAGE} makemigrations", shell=True)
    subprocess.call(f"{MANAGE} migrate", shell=True)
    if dev:
        subprocess.call(f"{MANAGE} populate", shell=True)


def front():
    """Run the Vue.js server."""
    subprocess.call(f"npm run --prefix frontend serve", shell=True)


def djapp(app):
    """Add a django app."""
    directory = f"./backend/apps/{app}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    command = f"{PIPENV} django-admin startapp {app} {directory}"
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    if os.name == 'nt':
        activate_colors_on_windows()

    args = docopt(__doc__)
    # print(args)

    true_args = [(key, value) for (key, value) in args.items() if value]
    statics = [(key, value) for (key, value) in true_args if "<" not in key]

    parameters = {key[1:-1]: value for (key, value) in true_args if "<" in key}
    options = {key[2:]: value for (key, value) in true_args if "-" in key}
    additionals = {**parameters, **options}

    for key, value in statics:
        thismodule = sys.modules[__name__]

        try:
            method = getattr(thismodule, key)
            method(**additionals)
        except TypeError:
            try:
                method()
            except TypeError:
                pass
        except AttributeError as error:
            pass
