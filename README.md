# CEN 4031 Final project

## Requirements

Please install both docker and the below python packages:

```
pip install flask sqlalchemy psycopg2-binary
```

## How To Run The Project

1. Start database in docker container

```
docker run --name titan-techs \
-e POSTGRES_PASSWORD=pass \
-e POSTGRES_USER=usr \
-e POSTGRES_DB=sqlalchemy \
-p 5432:5432 \
-d postgres
```

2. Checkout the source code and run

```
git clone https://github.com/rachaelfloto/group-project.git
cd group-project
python app.py
```

## Database

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
