from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from tasks.models import User, Task
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'add the database with users and project-related tasks'

    def handle(self, *args, **kwargs):
        # Define users
        users_data = [
            {
                'first_name': 'Ahmed',
                'last_name': 'Hamdy',
                'email': 'oreof00024@gmail.com',
                'password': '12345',
                'role': 'employee',
                'category': 'Backend',
            },
            {
                'first_name': 'Yoused',
                'last_name': 'Mostafa',
                'email': 'yoused@example.com',
                'password': '12345',
                'role': 'employee',
                'category': 'Frontend',
            },
            {
                'first_name': 'Mustafa',
                'last_name': 'Ali',
                'email': 'mustafa09402@gmial.com',
                'password': '12345',
                'role': 'employee',
                'category': 'DevOps',
            },
            {
                'first_name': 'Emad',
                'last_name': 'Kamal',
                'email': 'emadbadr227@gmail.com',
                'password': '12345',
                'role': 'employee',
                'category': 'Backend',
            },
            {
                'first_name': 'Ahmed',
                'last_name': 'Hamdy',
                'email': 'ahmedhandy06@gmail.com',
                'password': '12345',
                'role': 'manager',
                'category': '',
            },
        ]

        user_objects = {}

        for data in users_data:
            user, _ = User.objects.get_or_create(
                email=data['email'],
                defaults={
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'role': data['role'],
                    'category': data['category'],
                    'password': make_password(data['password']),
                    'birthday': timezone.now().date(),
                }
            )
            user_objects[data['email']] = user
            self.stdout.write(self.style.SUCCESS(f"Created/Found user {user.email}"))

        # Define tasks
        tasks_data = [
            # Ahmed's tasks
            {
                'title': 'Implement Manager Dashboard View',
                'description': 'Create a backend view to display manager-specific data and analytics.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },
            {
                'title': 'User Authentication Logic',
                'description': 'Develop login and registration mechanisms.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },
            {
                'title': 'Password Reset via OTP & Password Change',
                'description': 'Implement backend logic to send OTP to email for password reset, verify OTP, and allow users to set a new password.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },
            {
                'title': 'Task Category Model',
                'description': 'Create a model to define task categories and use them in task creation and filtering.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },
            {
                'title': 'Task Assignment Algorithm',
                'description': 'Implement logic to assign tasks to employees based on category and least number of uncompleted tasks.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },
            {
                'title': 'Implement Celery for Periodic Task Status Checks',
                'description': 'Set up Celery with Django to run periodic tasks that check and update the status of ongoing tasks regulary.',
                'assigned_to': user_objects['oreof00024@gmail.com'],
            },

            # Emad's tasks
            {
                'title': 'Build Employee List API',
                'description': 'Provide an endpoint to list, filter, and paginate employee records.',
                'assigned_to': user_objects['emadbadr227@gmail.com'],
            },
            {
                'title': 'Implement Employee Profile Update',
                'description': 'Enable backend logic to allow employees to update their info.',
                'assigned_to': user_objects['emadbadr227@gmail.com'],
            },

            # Yoused's tasks
            {
                'title': 'Design Task View Page (Frontend)',
                'description': 'Create a styled, responsive UI for task display for users.',
                'assigned_to': user_objects['yoused@example.com'],
            },
            {
                'title': 'Dark Theme Integration',
                'description': 'Apply black & orange dark theme across all frontend components.',
                'assigned_to': user_objects['yoused@example.com'],
            },

            # Mustafa's tasks
            {
                'title': 'Set Up CI/CD Pipeline',
                'description': 'Create GitHub Actions to auto deploy backend on commit.',
                'assigned_to': user_objects['mustafa09402@gmial.com'],
            },
            {
                'title': 'Dockerize Django Project',
                'description': 'Build and maintain Docker containers for dev and prod environments.',
                'assigned_to': user_objects['mustafa09402@gmial.com'],
            },
        ]

        priority_choices = ['low', 'medium', 'high']
        status_choices = ['pending', 'in_progress', 'completed']

        for task_data in tasks_data:
            created_at = timezone.now() - timedelta(days=random.randint(1, 10))
            deadline = created_at + timedelta(days=random.randint(10, 30))
            task = Task.objects.create(
                title=task_data['title'],
                description=task_data['description'],
                assigned_to=task_data['assigned_to'],
                created_at=created_at,
                deadline=deadline,
                priority=random.choice(priority_choices),
                status=random.choice(status_choices),
                category=task_data['assigned_to'].category
            )
            self.stdout.write(self.style.SUCCESS(f"Created task: {task.title} for {task.assigned_to.email}"))
