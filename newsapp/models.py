from django.db import models  # SQLite for authentication
from djongo import models as djongo_models  # MongoDB for news storage

class News(djongo_models.Model):
    title = djongo_models.CharField(max_length=500)
    content = djongo_models.TextField()
    department = djongo_models.CharField(max_length=100)
    sentiment = djongo_models.CharField(max_length=20, choices=[
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Neutral', 'Neutral')
    ])
    timestamp = djongo_models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"  # Make sure this matches your MongoDB collection name
        managed = False  # Ensures Django doesn't try to migrate this table

# ✅ SQLite Model for Authentication
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Django's auth system should handle hashing
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')])

    def __str__(self):
        return self.username
