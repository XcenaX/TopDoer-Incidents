# TopDoer-Incidents

```bash
git clone https://github.com/XcenaX/TopDoer-Incidents.git
cd TopDoer-Incidents
```

```bash
source .venv/bin/activate
```

```bash
python -m pip install -U pip
pip install -r requirements.txt
```

# миграции
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Как протестить
**Swagger** - http://127.0.0.1:8000/docs/
