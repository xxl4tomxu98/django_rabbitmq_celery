python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install django
django-admin startproject proj .
pip install celery
`sudo apt-get install rabbitmq-server` (or for macOS: `brew install rabbitmq`)
`sudo systemctl enable rabbitmq-server`
`sudo systemctl start rabbitmq-server` to start server (or for macOS: `brew services start rabbitmq`)
`sudo systemctl stop rabbitmq-server` to stop server (or for macOS: `brew services stop rabbitmq`)
`systemctl status rabbitmq-server` (to check if the server is working)
`celery -A proj worker -l info` (check if celery worker)
python manage.py shell
from app1.tasks import add
add.delay(4,4) (`Task app1.tasks.add[e21691c3-45bd-4a1f-86e1-55f46bffb272] received`, `Task app1.tasks.add[e21691c3-45bd-4a1f-86e1-55f46bffb272] succeeded in 0.0008664169999974547s: 8`)
add.apply_async((3,3), countdown=5) (`Task app1.tasks.add[77cbcf01-e768-4b26-9980-ab9e54cf81b6] received`, `Task app1.tasks.add[77cbcf01-e768-4b26-9980-ab9e54cf81b6] succeeded in 0.00028729200005273015s: 6`)