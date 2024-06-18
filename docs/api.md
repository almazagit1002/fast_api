# API
Test the end points localy by running: 
```
uvicorn main:app --reload 
```

 or specify the localhost
```
uvicorn main:app --reload --host localhost --port YOUR_PORT
```
 

And go to the docs:
```
 http://YOURLOCALHOST/docs
```
## End points

* Get Users
* Create User
* Get User by ID: only asynchronous endpoint
* Get User's Courses
* Get Courses
* Create Course
* Get Course by ID
* Update Course
* Delete Course
* Get Course Sections
* Get Section by ID
* Get Section Content Blocks
* Get Content Block by ID
