import os
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images from the media folder"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        updated_count = 0
        missing_count = 0

        for movie in movies:
            image_filename = f"m_{movie.title}.png"
            # Asignamos la ruta relativa de la imagen como lo espera Django
            movie.image = os.path.join('movie/images', image_filename)
            movie.save()
            updated_count += 1
            try:
                self.stdout.write(self.style.SUCCESS(f"Assigned image for: {movie.title}"))
            except UnicodeEncodeError:
                self.stdout.write(self.style.SUCCESS(f"Assigned image for: [Movie with special characters]"))

        self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated_count} movies with images from folder."))
