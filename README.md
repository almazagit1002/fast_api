# Fast API 


## Prerequisites
Before running the FastAPI API and client examples, make sure you have the following installed:

Python (version >= 3.11)

## Installation
Clone the Repository:


```bash
git clone https://github.com/almazagit1002/fast_api.git
```

Navigate to the Project Directory:
```bash
cd fast_api
```

Set Up Python Virtual Environment (Optional but Recommended):
```bash
python3 -m venv venv
```

```bash
.\venv\Scripts\activate
```

Install Dependencies:

```bash
pip install poetry
```

```bash
poetry install
```

Create initial documentation
To create mkdocs run:
```bash
mkdocs new .
```

## Run API in localhost

```bash
uvicorn main:app --reload 
```
 or specify the localhost
```bash
uvicorn main:app --reload --host localhost --port YOUR_PORT
```
 

## Documentation 

See documentation in local host running: 
```bash
mkdocs serve 
```
or specify the localhost
```bash
mkdocs serve -a localhost:YOUR_PORT
```
