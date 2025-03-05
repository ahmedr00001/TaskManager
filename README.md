# Task Manager App

## Project Overview

The **Task Manager App** is a web-based application designed to help managers and employees track tasks efficiently. It allows managers to create, update, and delete tasks, while employees can view and update their assigned tasks.

## Installation and Setup

```bash
git clone https://github.com/MUSTAFA-3LI/Fork_TaskManager
python -m venv venv
source venv/bin/activate # For Linux
venv\Scripts\activate    # For Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## User Guide

### Manager Role

**Logging In**: Use manager credentials to access the admin dashboard.

![Image](https://github.com/user-attachments/assets/1ad5d251-2ca2-4081-bd85-b767c171bdb4)

**Manage Tasks**:

1. Create, update, and delete tasks.

2. Assign tasks to employees.

3. Filter tasks by status (completed, delayed, in progress).

**Monitor Employees**:

1. View employee task statistics.
2. Track task completion rates.

![Image](https://github.com/user-attachments/assets/da9aa6c5-74f0-41e7-b9ab-28e1bfacc74b)

### Employee Role

1. **Logging In**: Use employee credentials to access the dashboard.

2. **View Tasks**: Employees can see their assigned tasks.

3. **Update Task Status**: Employees can update the progress of their assigned tasks.

![Image](https://github.com/user-attachments/assets/1ead928e-d503-42ec-909b-6d37b420adea)

### Managing Tasks:

**Log in as a manager.**

**Click the `Add Task` button.**

**Fill in the task details:**

1. Title
2. Description
3. Priority
4. Status
5. Due date

**Click `Add` to save the task.**

![Image](https://github.com/user-attachments/assets/9963cefc-bcb6-4862-b6b2-a73608350935)

## Database Models

### User Model

1. Represents users (Managers and Employees).

2. Contains login credentials, roles, and related information like phone number and birthdate.

### Task Model

**Represents tasks assigned to employees.**

Includes:

1. Title: Task name.
2. Description: Task details.
3. Priority: Low, Medium, High.
4. Status: Completed, In Progress and Delayed.
5. Due Date: Task deadline.

## Planned Features

1. **Notifications**: Alert users about upcoming task deadlines.

2. **automatic Task Assignment**: The system will automatically assign tasks to employees based on predefined criteria.

3. **Enhanced User UI**
