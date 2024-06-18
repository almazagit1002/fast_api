# Data Base

The code sets up database connections (engine and async_engine) for synchronous and asynchronous operations using SQLAlchemy.
It defines session factories (SessionLocal and AsyncSessionLocal) tailored for synchronous and asynchronous sessions, respectively.
get_db() and async_get_db() functions provide utility methods to retrieve database sessions synchronously and asynchronously, demonstrating the difference in handling sessions between synchronous and asynchronous contexts.

## Database Setup

The database setup uses SQLAlchemy for both synchronous and asynchronous operations. Below is the configuration and setup code:

### Environment Variables
Make sure to set the following environment variables, and create .env file with these variables:

* DB_USERNAME: Your database username
* DB_PASSWORD: Your database password
* DB_HOST: The host of your PostgreSQL database
* DB_NAME: The name of your PostgreSQL database

### URL's

* SQLALCHEMY_DATABASE_URL: This is a SQLAlchemy-compatible database URL for PostgreSQL using the psycopg2 driver. It includes the username, password, host, and database name.

* ASYNC_SQLALCHEMY_DATABASE_URL: This URL is specifically tailored for asynchronous operations using asyncpg, which is an async-friendly PostgreSQL database driver for Python.

### Engine Creration

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)

```

* engine: This creates a synchronous SQLAlchemy engine using create_engine. It connects to the PostgreSQL database specified by SQLALCHEMY_DATABASE_URL. The future=True parameter enables SQLAlchemy's async I/O support for executing queries asynchronously in the future.

* async_engine: This creates an asynchronous SQLAlchemy engine using create_async_engine. It connects to the same PostgreSQL database but is optimized for asynchronous operations using asyncpg.

### Session Creation

```python
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

```

* SessionLocal: This is a factory function (sessionmaker) that creates SQLAlchemy sessions for synchronous operations. It uses the synchronous engine created earlier. autocommit=False and autoflush=False are SQLAlchemy session parameters that control session behavior.

* AsyncSessionLocal: This creates an asynchronous session factory for use with async operations. It uses the async_engine and specifies class_=AsyncSession to indicate it should use AsyncSession for asynchronous transactions. expire_on_commit=False prevents objects from being expired after commit in async sessions.

### Base Declaration
 
 ```python
 Base = declarative_base()

 ```

 * Base is the base class for declarative class definitions in SQLAlchemy. It is used as a base class for ORM models (database tables). Any ORM model class should inherit from Base.
 (An Object-Relational Mapping (ORM) model provides a structured way to map database tables to object-oriented classes, enabling seamless interaction between application code and relational databases. It abstracts away database complexities and enhances productivity and maintainability in software development projects.)

### DB Utilities

 ```python
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    async def async_get_db():
        async with AsyncSessionLocal() as db:
            yield db
            await db.commit()

 ```

 * get_db(): This is a synchronous function that yields a session (db) from SessionLocal. The session is used within a context (try block) where it can be accessed by the caller. After the caller finishes using the session (yield), the finally block ensures that the session is closed properly.

* async_get_db(): This is an asynchronous function (async def) that uses an asynchronous context manager (async with) to manage the session (db) from AsyncSessionLocal. Within the context, it yields the session to the caller for use. The await db.commit() line demonstrates an async operation where the session is committed asynchronously.

## Notes on Asynchronous Usage
Asynchronous programming is a programming paradigm that allows tasks to run concurrently without blocking other tasks. In traditional synchronous programming, each operation executes one after the other, blocking the execution until completion. Asynchronous programming, on the other hand, allows tasks to overlap in execution, enabling better utilization of resources and improving overall system responsiveness.

AsyncSession in SQLAlchemy provides a powerful mechanism for handling asynchronous database operations in Python applications. It leverages asynchronous programming principles to enhance performance and scalability but requires careful consideration of its complexities and resource management aspects. Integrating AsyncSession effectively can significantly benefit applications that require high concurrency and responsiveness.

### Advantages of Asynchronous Programming

* Concurrency: Asynchronous programs can execute multiple tasks concurrently, which is essential for handling I/O-bound operations efficiently.
* Improved Performance: By avoiding blocking operations, asynchronous programs can make better use of CPU cycles and reduce waiting time.
* Scalability: Asynchronous programming can handle more requests concurrently compared to synchronous programming, making it suitable for scalable applications.

### Disadvantages of Asynchronous Programming

* Complexity: Asynchronous programming introduces complexity due to the need for managing asynchronous tasks, callbacks, and potential race conditions.
* Debugging: Debugging asynchronous code can be more challenging than synchronous code because of its non-linear execution flow.
* Learning Curve: Developers accustomed to synchronous programming may find it challenging to transition to asynchronous programming due to its different paradigm.

### Implementation

The only end point using AsyncSession is `Get User by ID`