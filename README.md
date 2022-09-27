# group-project

## Requirements

Please install both docker and the below python packages:

```
pip install flask sqlalchemy psycopg2-binary
```

## Database

To create and start the database:

```bash
docker run --name titan-techs \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
```

To stop the database:

```
docker stop titan-techs
```

To start the database:

```
docker start titan-techs
```

To delete the database:

```
docker rm titan-techs
```
