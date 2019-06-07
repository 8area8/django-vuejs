"""Automation script.

Usage:
  run.py back
  run.py front
  run.py pop
  run.py -h

Arguments:
  back          run the django server
  front         run the Vue.js server
  pop           populate the django database

Options:
  -h --help     Show this screen.

"""

import os
import sys
import subprocess

from docopt import docopt
import colorama


MANAGE = "pipenv run python manage.py"


def activate_colors_on_windows():
    """Colors in the shell."""
    colorama.init()
    os.environ['ANSICON'] = 'on'


def back():
    """Run the Django server."""
    subprocess.call(f"{MANAGE} runserver", shell=True)


def pop():
    """Populate the database."""
    subprocess.call(f"{MANAGE} makemigrations", shell=True)
    subprocess.call(f"{MANAGE} migrate", shell=True)


def front():
    """Run the Vue.js server."""
    subprocess.call(f"npm run --prefix frontend serve", shell=True)


if __name__ == '__main__':
    if os.name == 'nt':
        activate_colors_on_windows()

    args = docopt(__doc__)
    # print(args)

    for key, is_true in args.items():
        if is_true:
            thismodule = sys.modules[__name__]

            try:
                method = getattr(thismodule, key)
                method()
            except AttributeError:
                print(f"No attribute called {key}.")
            except TypeError:
                print(f"No function called {key}.")
