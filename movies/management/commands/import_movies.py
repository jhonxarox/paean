import json
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Import movies from JSON file'

    def handle(self, *args, **kwargs):
        with open('movies.json') as file:
            data = json.load(file)
            for movie in data:
                Movie.objects.create(
                    name=movie['name'],
                    description=movie['description'],
                    img_path=movie['imgPath'],
                    duration=movie['duration'],
                    genre=movie['genre'],
                    language=movie['language'],
                    mpaa_rating_type=movie['mpaaRating']['type'],
                    mpaa_rating_label=movie['mpaaRating']['label'],
                    user_rating=int(movie['userRating']),
                )
        self.stdout.write(self.style.SUCCESS('Movies imported successfully'))
