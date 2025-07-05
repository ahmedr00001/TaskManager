# DistriTask

A comprehensive web-based task management system designed to streamline organizational workflow and enhance team collaboration. DistriTask supports two distinct user roles: Manager and Employee, with advanced features including real-time chat, AI chatbot assistance, and secure API authentication.

<img width="1903" height="915" alt="Image" src="https://github.com/user-attachments/assets/3ab8a439-69f7-4891-9129-9c648f715426" />

##  Table of Contents

- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Development & Testing](#development--testing)
- [Core Features](#core-features)
- [API Overview](#api-overview)


##  Key Features

- **Secure Authentication**: Role-based access for Managers and Employees
- **Intelligent Task Assignment**: Automatic task distribution based on workload
- **Real-Time Chat**: Instant messaging with WebSocket support
- **AI-Powered Chatbot**: Natural language interaction for task queries and automation
- **Comprehensive Analytics**: Dashboards for task completion and performance tracking
- **Mobile-Responsive Design**: Seamless experience across devices

##  Technologies Used

### Backend
- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **Django Channels** (WebSockets)
- **Celery** (Task Queue)
- **Redis** (Message Broker & Cache)

### Database
- **MySQL** or **SQLite**

### Authentication
- **Django's built-in authentication**
- **Token authentication** for API access

### Testing
- **pytest**
- **Django test framework**

##  Installation

Follow these steps to set up and run DistriTask locally:

### 1. Clone the repository

```bash
git clone https://github.com/MUSTAFA-3LI/DistriTask
cd task-manager
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure settings

Update `TaskManager/settings.py` with:

- Database settings (SQLite or MySQL)
- Email backend credentials
- Redis settings for Celery and Channels
- Static and media file configurations

### 5. Set up database

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

##  Development & Testing

Before starting the server, ensure all tests pass to maintain code quality.

### Running Tests

```bash
python manage.py test
# or
pytest
```

> **Test Coverage**: The project includes comprehensive test coverage for all core functionalities.

![Image](https://github.com/user-attachments/assets/2b0e842f-2a02-4c6d-805f-8c873a1c566a)

### Starting Services

Now, you can start the necessary services and the development server:

#### 1. Start Redis server (for Celery and Channels)

```bash
redis-server
```

#### 2. Start Celery worker (in a new terminal)

```bash
celery -A TaskManager worker -l info
```

#### 3. Start development server

```bash
python manage.py runserver
```

##  Core Features

### Authentication & User Management

DistriTask features a robust authentication system allowing users to securely log in and manage their accounts. It supports a custom user model with email-based login, password reset functionality via OTP, and comprehensive role-based access control for Managers and Employees.

**Features:**
- **Custom User Model**: Email login and secure password management
- **Role-Based Access Control**: Distinct permissions for Managers and Employees
- **Session-Based Login/Logout**: Standard web session management
- **Token-Based API Authentication**: Secure access for all API interactions
- **Password Reset**: Via OTP sent to the registered email
- **CSRF Protection**: Enhanced security against cross-site request forgeries

<img width="1919" height="915" alt="Image" src="https://github.com/user-attachments/assets/82ed96bd-b407-4214-9663-7e871d36d01f" />
<img width="1917" height="925" alt="Image" src="https://github.com/user-attachments/assets/e2c9ce14-72da-4720-81a0-2f0fd29f41cd" />
### Intelligent Task Management (Manager View)

Managers have full control over task creation, assignment, and monitoring. The system incorporates an intelligent algorithm that automatically assigns tasks to employees based on workload balancing and specific categories, ensuring optimal distribution and efficiency.

**Features:**
- **Task Creation, Editing, Deletion**: Full CRUD operations for tasks
- **Automatic Assignment**: Tasks are intelligently assigned to the employee with the least uncompleted tasks within a given category
- **Task Status Tracking**: Monitor tasks as pending or completed
- **Categories & Deadlines**: Organize tasks with categories and strict deadlines
- **Filtering & Searching**: Easily view tasks by status, assigned employee, or category
- **Task ID Lookup**: Quickly find tasks by their title

<img width="1909" height="921" alt="Image" src="https://github.com/user-attachments/assets/1ab329e7-76d4-4472-a218-8c7ab89f87f9" />
<img width="1907" height="921" alt="Image" src="https://github.com/user-attachments/assets/3f9c553d-67b5-45cd-847e-9ef2c6d486df" />
### Employee Task View

Employees are provided with a streamlined interface to view only the tasks assigned to them. They can track the status of their tasks, mark them as completed, and manage their workload effectively within the given deadlines.

**Features:**
- **Personalized Task List**: Employees only see tasks assigned specifically to them
- **Task Status Updates**: Ability to mark tasks as completed
- **Deadline Awareness**: Clear visibility of task deadlines

<img width="1920" height="920" alt="Image" src="https://github.com/user-attachments/assets/89676c4f-6f7f-461f-9d2c-0c997f80398a" />
### Real-Time Communication

DistriTask integrates a WebSocket-based chat system using Django Channels, enabling seamless real-time communication between team members.

**Features:**
- **WebSocket-Based Chat**: Powered by Django Channels for instant messaging
- **Team Collaboration**: Dedicated chat rooms for different teams or projects
- **Message History**: Access to past conversations for continuity
- **Read Status Tracking**: Know when your messages have been seen

<img width="1919" height="925" alt="Image" src="https://github.com/user-attachments/assets/93f093f8-b7ba-47f3-b029-a3268f82088f" />
### AI Chatbot Assistant

An intelligent chatbot assistant powered by natural language processing provides instant support for task-related queries and automates common operations.

**Features:**
- **Natural Language Processing**: Understands and responds to natural language queries
- **Task-Related Queries**: Get instant answers on task statuses, deadlines, and details
- **Quick Actions**: Perform common operations like task reassignment or status updates
- **Multi-Step Interactions**: Supports complex operations requiring multiple conversational turns
- **Performance Analytics**: Retrieve statistics on task completion rates, employee performance, and more

<img width="1905" height="915" alt="Image" src="https://github.com/user-attachments/assets/7739e01a-ce94-4f07-b4f9-798e5f0e8428" />
##  API Overview

### Chatbot API Endpoints (Token Authentication Required)

| Endpoint                       | Method | Description                         |
| ------------------------------ | ------ | ----------------------------------- |
| `/chatbot/total-tasks/`        | GET    | Get total task count                |
| `/chatbot/completed-tasks/`    | GET    | Get completed tasks statistics      |
| `/chatbot/delayed-tasks/`      | GET    | Get delayed tasks information       |
| `/chatbot/overdue-tasks/`      | GET    | Get overdue tasks list              |
| `/chatbot/top-employees/`      | GET    | Get top performing employees        |
| `/chatbot/completion-rate/`    | GET    | Get overall completion rate         |
| `/chatbot/tasks-due-on/`       | GET    | Get tasks due on specific date      |
| `/chatbot/tasks-per-category/` | GET    | Get tasks by category               |
| `/chatbot/tasks-for-user/`     | GET    | Get tasks assigned to specific user |
| `/chatbot/user-info/`          | GET    | Get user information                |
| `/chatbot/task-id/`            | GET    | Get task ID by title                |
| `/chatbot/reassign-task/`      | POST   | Reassign task to different user     |



### General API Endpoints

DistriTask provides a comprehensive set of RESTful API endpoints built with Django REST Framework, ensuring secure and efficient data exchange for all functionalities. All API endpoints are protected with token authentication and CSRF protection.

| Endpoint                   | Method | Description               |
| -------------------------- | ------ | ------------------------- |
| `/chatbot/api-token-auth/` | POST   | Get API token for chatbot |

