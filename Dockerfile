FROM rasa/rasa-sdk:3.1.2

WORKDIR /app

COPY . /app

# Fix pip permission + speed up build
ENV PIP_NO_CACHE_DIR=yes
ENV PIP_ROOT_USER_ACTION=ignore
ENV PATH="${PATH}:/root/.local/bin"

RUN pip install -r requirements.txt

CMD ["rasa", "run", "actions"]