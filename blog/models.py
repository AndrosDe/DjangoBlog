from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    ''' The content of a post '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ''' Will order Posts in a decending order '''
        ordering = ['-created_on']

    def __str__(self):
        ''' Displaying the title of a post '''
        return self.title

    def number_of_likes(self):
        ''' Displaying the number of likes on a post '''
        return self.likes.count()


class Comment(models.Model):
    '''The content of the comments '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        Will order Posts in a ascending order
        -> oldest comment first
        '''
        ordering = ['created_on']

    def __str__(self):
        '''
        Displaying the comment and the  author of that comment to the post
        '''
        return f"Comment {self.body} by {self.name}"
