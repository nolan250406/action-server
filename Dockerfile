FROM rasa/rasa-sdk:3.1.2

USER root
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY actions /app/actions

CMD ["start", "--actions", "actions", "--debug"]