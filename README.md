# coinmena
BTC/USD Api

## Endpoints:
GET /api/v1/quotes => get latest BTC price in USD
POST /api/v1/quotes  => get up to date BTC price in USD

I assumed that there's a separate system to generate access tokens, for the purposes of this task, the "token" value should be 123456

I implemented 2 environments, development and production
There should be an .env.dev or .env.prod file in the root directory, depending on which environment you'd like to build


## Example .env.dev:

DEBUG=1

SECRET_KEY=alsfhsafhbclkscadjhfawewerybnmliwury

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql

SQL_DATABASE=coinmena

SQL_USER=coinmena

SQL_PASSWORD=coinmena

SQL_HOST=db

SQL_PORT=5432

DATABASE=postgres



ALPHA_VANTAGE_APIKEY=XT4QIULYRC2LYKLI

UPDATE_DURATION=60


## Example .env.prod

DEBUG=0

SECRET_KEY=change_me

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql

SQL_DATABASE=coinmena

SQL_USER=coinmena

SQL_PASSWORD=coinmena

SQL_HOST=db

SQL_PORT=5432

DATABASE=postgres



ALPHA_VANTAGE_APIKEY=XT4QIULYRC2LYKLI

UPDATE_DURATION=60
