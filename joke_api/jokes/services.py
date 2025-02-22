from .models import Joke

def get_all_jokes(category=None):
    """Retrieve all jokes, optionally filtering by category."""
    jokes = Joke.objects.all()
    if category:
        jokes = jokes.filter(category__iexact=category)  # Case-insensitive filtering
    return jokes

def get_joke_by_id(joke_id):
    return Joke.objects.filter(id=joke_id).first()

def create_joke(data):
    return Joke.objects.create(**data)

def update_joke(joke, data):
    for key, value in data.items():
        setattr(joke, key, value)
    joke.save()
    return joke

def delete_joke(joke):
    joke.delete()

