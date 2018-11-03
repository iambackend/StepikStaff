sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
curl 0.0.0.0:8080/?a=1&b=34&c=1488
curl 127.0.0.1:80/hello/?a=1&b=34&c=1488
# gunicorn -b 0.0.0.0:8080 hello.py:app