from django.db import models

class Joke(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('programming', 'Programming'),
        ('knock-knock', 'Knock-Knock'),
        ('funny', 'Funny'),
        ('puns', 'Puns'),
    ]

    setup = models.TextField()
    punchline = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    def save(self, *args, **kwargs):
        if self.rating is not None and (self.rating < 1 or self.rating > 5):
            raise ValueError("Rating must be between 1 and 5.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.setup
