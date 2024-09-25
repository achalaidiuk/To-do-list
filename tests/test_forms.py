from django.test import TestCase
from todolist_project.forms import TaskCreationForm, TagsCreationForm
from todolist_project.models import Tag


class TaskCreationFormTest(TestCase):
    def test_valid_form(self):
        tag = Tag.objects.create(name="Test Tag")
        form_data = {
            "content": "Test Task",
            "deadline": "2024-12-31",
            "tags": [tag.id],
        }
        form = TaskCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_without_content(self):
        form_data = {
            "content": "",
            "deadline": "2024-12-31",
            "tags": [],
        }
        form = TaskCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)


class TagsCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "Test Tag",
        }
        form = TagsCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_without_name(self):
        form_data = {
            "name": "",
        }
        form = TagsCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
