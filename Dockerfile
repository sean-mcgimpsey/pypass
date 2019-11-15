FROM python:3.7.3-alpine

COPY password /opt/password
RUN pip install -r /opt/password/requirements.txt; chmod +x /opt/password/docker-entrypoint.sh
ENV FLASK_APP=/opt/password/app/password.py 
WORKDIR /opt/password
CMD ["/bin/sh", "./docker-entrypoint.sh"]