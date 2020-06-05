**How ToDO**
=====================

1. копируем сервис в /etc/systemd/sytem
2. копируем скрипт в /usr/bin/
3. systemctl daemon-reload
4. systemctl enable test3.service
5. systemctl start test3.service
6. systemctl status test3.service - смотрим, что у нас все хорошо, если нет - смотрим на ошибки
7. systemctl stop test3.service - остановка
8. в отдельной консоли journalctl -f -u test3 - тут все выводы сервиса 
