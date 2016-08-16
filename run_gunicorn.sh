bash init.sh
gunicorn -c /etc/gunicorn.d/test.conf ask.wsgi &
