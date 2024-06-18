# Alembic
For using Alembic with FastAPI to perform data migrations and initial data insertion, you'll follow a the following approach. Alembic primarily handles schema migrations, but you can include data insertion in the migration script's upgrade function to initialize your database with the provided data. Here’s how you can achieve this:

## Setting up Alembic with FastAPI

### Set Up Alembic Configuration

Create an Alembic configuration file (alembic.ini). This file specifies how Alembic should connect to your database.

```
alembic init
```
In alembic.ini, update the line with your databse configuration
```
sqlalchemy.url= postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}
```
### Generate Initial Migration

Use Alembic to generate an initial migration that includes creating tables and inserting initial data.
```
alembic revision --autogenerate -m "Initial schema and data"

```
This command generates a new migration script in your alembic/versions directory.

### Edit Migration Script

Open the generated migration script (alembic/versions/*.py) and modify the upgrade() function to insert the initial data.

Adjust the schema and data according to your specific requirements.

### Run Migrations
Apply the migration to your database:
```
alembic upgrade head

```

## Alembic Documentation

Follow the oficial documentation: 

[Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
