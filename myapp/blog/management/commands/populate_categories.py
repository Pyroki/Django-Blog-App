from blog.models import Post,Category
from django.core.management.base import BaseCommand
 


class Command(BaseCommand):
    help="this command is used to insert the data"

    def handle(self, *args, **options):
        #detele existing data
        Category.objects.all().delete()

        categories=['sports','education','science','skils','knowledge']
   


        for category_name in categories:
            Category.objects.create(name=category_name)
            
        
        self.stdout.write(self.style.SUCCESS('completed insertig data!!'))        
    