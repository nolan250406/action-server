FROM rasa/rasa-sdk:3.1.2

WORKDIR /app

COPY . /app

# 👉 Bỏ lỗi permission denied
ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5055

CMD ["rasa", "run", "actions"]