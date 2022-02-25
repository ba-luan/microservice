FROM python3

WORKDIR /usr/src/app

COPY . .

CMD ./post_text_ad.py