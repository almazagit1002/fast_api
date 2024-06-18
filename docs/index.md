# Fast API tutorial

Tutorial created by following:

<a href="https://www.youtube.com/watch?v=gQTRsZpR7Gw&t=9383s" target="_blank">Watch on YouTube</a>

## API

In order to run the API use:
```bash
uvicorn main:app --reload 
```

or specify the localhost
```bash
uvicorn main:app --reload --host localhost --port YOUR_PORT
```
 
### Overview

This API provides CRUD operations (GET, POST, PATCH, and DELETE) for a PostgreSQL database representing a fictional course management system. The database includes entities such as users (students), courses, and sections. The API is written in Python 3.11 and utilizes SQLAlchemy for ORM.


## Project layout
```
|__fast_api
    |__alembic/
        |__data/
            |__students.json
            |__env.py
    |__api/
        |__utils/
            |__courses.py
            |__users.py
        |__courses.py
        |__users.py
        |__sections.py
    |__db/
        |__models/
            |__course.py
            |__mixins.py
            |__users.py
        |__db_setup.py
    |__pydantic_schemas/
        |__courses.py
        |__users.py
    |__main.py
```