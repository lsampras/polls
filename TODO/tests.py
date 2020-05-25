from django.test import TestCase
from django.utils import timezone

from .models import TODO
from .views import update

from django.http import HttpRequest

# Create your tests here.

class TODOModelTests(TestCase):

    def test_todo_was_marked_as_complete(self):

        t = TODO(task="Test",date=timezone.now())
        t.save()
        update(HttpRequest(), t.pk)
        t.refresh_from_db()
        self.assertIs(t.done, True)