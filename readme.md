## This project dedicated for Assesment Test Modana

This readme guide you to run this project. Follow the step correctly.

1. Make sure you has the project folder. Clone the repo in `https://github.com/hkkundo/modana_django_hari.git`.
2. Open Terminal and install virtual environment python for this project. You can install outside or inside the project. Type `python -m venv [virtual-environment-name]` on your terminal.
3. Activate virtual environment python. `[virtual-environment-name]/bin/activate`.
4. Install package required. Type in your terminal `pip install -r requirements.txt`
5. In folder **modana_django_hari** add file named *settings.ini*
6. Add text `[settings]
SECRET_KEY=4f#y0sz*szj1dq!u)k_l1s3wqt&$q)6i(hc-at7rrtw1$8+8#t
DEBUG=True
ALLOWED_HOSTS=localhost
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=modana_django_hari
DB_USER=[dbname]
DB_PASS=
DB_HOST=[dbhost]
DB_PORT=[dbport]` in settings.ini
6. Migrate models in project `python manage.py migrate`.
7. Run project `python manage.py runserver`. And the project start! Enjoy.