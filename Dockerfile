FROM fsheets_base:latest
COPY conf /srv/flask_app
WORKDIR /srv/flask_app

RUN chmod +x ./start.sh
CMD ["./start.sh"]