# Todo List Project

This is a simple Todo List web application built with Django. It allows users to create, update, delete, and manage tasks with optional deadlines and tags.

## Features

- Create, update, and delete tasks.
- Mark tasks as completed or not completed.
- Add, update, and delete tags.
- View a list of tasks ordered creation date.
- View a list of tags.

## Models

### Task

- `content`: Text field to describe the task.
- `created_at`: Datetime field for when the task was created.
- `deadline`: Optional datetime field for the task's deadline.
- `is_done`: Boolean field indicating if the task is done.
- `tags`: Many-to-many relationship with the `Tag` model.

### Tag

- `name`: Name of the tag.

## Pages

### Home Page (`/`)

- Displays a list of tasks ordered from not done to done and from newest to oldest.
- Includes a sidebar with links to the home page and tag list page.
- Shows task information including content, creation datetime, deadline, status, and tags.
- Provides buttons to add a new task, update, delete, complete/undo tasks.
![image](https://github.com/user-attachments/assets/5fd75f65-b363-4320-8099-7eacb5501ddf)
![image](https://github.com/user-attachments/assets/cd9ec0b4-29b3-4360-b9df-a494631c5992)
![image](https://github.com/user-attachments/assets/a25986d6-9d41-46ff-a29a-31fe5a52f31f)

### Tag List Page (`/tags/`)

- Displays a table of tags with names, update links, and delete links.
- Includes a button to add a new tag.
- Contains a sidebar with links to the home page and tag list page.
![image](https://github.com/user-attachments/assets/6237fe1e-34bb-401c-b271-fb9257967dde)
![image](https://github.com/user-attachments/assets/0e5b13c5-f567-4370-bef4-c27be0bfd9be)
![image](https://github.com/user-attachments/assets/5860a96f-e1f9-442e-b04c-3c7b69eaeee9)


## Installation

## Installation Instructions

> 👉 Download the code  

```bash
$ git clone https://github.com/OLENA-KALITSINSKA/todo-list.git
$ cd todo_list
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```
