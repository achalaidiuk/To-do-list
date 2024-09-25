from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from todolist_project.models import Task, Tag

User = get_user_model()


class TaskViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task",
                                        is_completed=False)
        self.task.tags.add(self.tag)


    def test_task_create_view(self):
        response = self.client.post(reverse("todolist_project:task-create"), {
            "content": "New Task",
            "is_completed": False,
            "tags": [self.tag.id]
        })
        self.assertEqual(response.status_code,
                         302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())


    def test_task_list_view(self):
        response = self.client.get(reverse("todolist_project:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todolist_project/task_list.html")
        self.assertContains(response, "Test Task")
