FROM rasa/rasa-sdk:3.1.2

WORKDIR /app
COPY ./actions /app/actions
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5055

CMD ["rasa", "run", "actions"]