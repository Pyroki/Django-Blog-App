from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random
 


class Command(BaseCommand):
    help="this command is used to insert the data"

    def handle(self, *args, **options):
        #detele existing data
        Post.objects.all().delete()
        titles = [
    "Mastering Django Basics",
    "Understanding Python Models",
    "Building Dynamic Web Applications",
    "Creating Custom 404 Pages",
    "Exploring Django Views",
    "Getting Started with URLs",
    "Introduction to Django Templates",
    "Handling Forms in Django",
    "Implementing User Authentication",
    "Working with Databases in Django",
    "Optimizing Django Performance",
    "Developing Blog Applications",
    "Using Static Files in Django",
    "Advanced Django Middleware",
    "Setting Up Django Admin Panel",
    "Debugging Django Applications",
    "Deploying Django Projects",
    "Creating REST APIs with Django",
    "Understanding Querysets and ORM",
    "Handling Errors Gracefully in Django",
]

        contents = [
    "Learn the foundational concepts of Django and start building projects.",
    "Discover how to define and work with models in Django applications.",
    "Create dynamic, interactive websites using Django's powerful framework.",
    "Implement custom error pages to improve user experience.",
    "Understand how to handle HTTP requests and return responses in Django.",
    "Set up and configure URL patterns for seamless navigation.",
    "Dive into Django templates and use them to build engaging UIs.",
    "Learn how to manage user input effectively with Django forms.",
    "Secure your applications with Django's authentication system.",
    "Connect and interact with databases using Django's ORM.",
    "Explore techniques to make Django applications faster and more efficient.",
    "Step-by-step guide to developing a blog application in Django.",
    "Understand the setup and use of static files for styling and scripts.",
    "Gain insights into the power and customization of Django middleware.",
    "Learn how to configure and optimize the Django admin interface.",
    "Debugging best practices to handle issues during development.",
    "Learn the process of deploying Django applications to production.",
    "Build RESTful APIs using Django for modern web applications.",
    "Master querysets and ORM to efficiently fetch and manipulate data.",
    "Handle errors and exceptions gracefully for a polished user experience.",
]

        img_urls = [
    "https://picsum.photos/id/1/400/800",
    "https://picsum.photos/id/2/400/800",
    "https://picsum.photos/id/3/400/800",
    "https://picsum.photos/id/4/400/800",
    "https://picsum.photos/id/5/400/800",
    "https://picsum.photos/id/6/400/800",
    "https://picsum.photos/id/7/400/800",
    "https://picsum.photos/id/8/400/800",
    "https://picsum.photos/id/9/400/800",
    "https://picsum.photos/id/10/400/800",
    "https://picsum.photos/id/11/400/800",
    "https://picsum.photos/id/12/400/800",
    "https://picsum.photos/id/13/400/800",
    "https://picsum.photos/id/14/400/800",
    "https://picsum.photos/id/15/400/800",
    "https://picsum.photos/id/16/400/800",
    "https://picsum.photos/id/17/400/800",
    "https://picsum.photos/id/18/400/800",
    "https://picsum.photos/id/19/400/800",
    "https://picsum.photos/id/20/400/800",
]

        categories=Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        
            
        
        self.stdout.write(self.style.SUCCESS('completed insertig data!!'))        
    