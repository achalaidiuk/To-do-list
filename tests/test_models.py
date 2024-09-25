from django.test import TestCase
from todolist_project.models import Tag, Task


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Urgent")
        self.assertEqual(str(self.tag), "Urgent")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")
        self.task = Task.objects.create(
            content="Finish the project",
            is_completed=False,
        )
        self.task.tags.add(self.tag)

    def test_task_creation(self):
        self.assertEqual(self.task.content, "Finish the project")
        self.assertFalse(self.task.is_completed)
        self.assertIsNone(self.task.deadline)
        self.assertIsNone(self.task.done_at)

    def test_task_tag_association(self):
        self.assertIn(self.tag, self.task.tags.all())

    def test_task_deadline(self):
        self.task.deadline = "2024-12-31"
        self.task.save()
        self.assertEqual(self.task.deadline, "2024-12-31")
