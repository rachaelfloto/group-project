# group-project

## Requirements

Please install both docker and the below python packages:

```
pip install flask sqlalchemy psycopg2-binary
```

## Database

To create and start the database:

```bash
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
```

To stop the database:

```
docker stop sqlalchemy-orm-psql
```

To start the database:

```
docker start sqlalchemy-orm-psql
```

To delete the database:

```
docker rm sqlalchemy-orm-psql
```
