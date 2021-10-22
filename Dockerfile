FROM python:3.9.5-alpine

RUN pip install --upgrade pip

RUN adduser -D dockeruser
USER dockeruser

WORKDIR /home/dockeruser
COPY --chown=dockeruser:dockeruser requirements.txt requirements.txt

RUN pip install --user -r requirements.txt

ENV PATH="/home/dockeruser/.local/bin:${PATH}"
COPY --chown=dockeruser:dockeruser . .

CMD [ "waitress-serve", "--port=5000" , "--call", "app:create_app"]
