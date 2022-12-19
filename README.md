# ToDo App :memo: 
Get organized and keep track of all the tasks you need to do with the ToDo app

## Features
Using the app, you will be able to manage your tasks by:

- Adding new tasks

- Editing existing tasks

- Deleting completed tasks

## How to run the app
### Instructions
1. Open CMD/Terminal and run the following command:

```
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/ToDo_App
```

2. Then go inside the Backend folder:

```
cd Backend
```

3. Then to build an image, run the following command:

```
docker build -t Backend .
```

4. Then to build a container, run the following command:

```
docker run -p 8000:8000 Backend
```

5. The app is running, now all you have to do is to open your browser and type:

```
http://localhost:8000/
```

## Technologies
This app was built with the following technologies:

- Backend: FastAPI (Python)

- Frontend: React (JavaScript)

