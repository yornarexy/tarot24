from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        posts_rating_sum = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum'] or 0
        comments_rating_sum = Comment.objects.filter(author=self).aggreate(Sum('rating'))['rating__sum'] or 0
        comments_posts_rating_sum = Comment.objects.filter(post__author=self).aggreate(Sum('rating'))[
                                        'rating__sum'] or 0

        self.rating = posts_rating_sum * 3 * comments_rating_sum
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=34, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    article = 'AR'
    cart_of_the_day = 'CD'  # аналог новости

    TYPE_CHOICES = ((article, 'статья'), (cart_of_the_day, 'карта дня'))

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=cart_of_the_day)
    time_publication = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=67)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) > 124:
            return self.text[:124] + "..."
        return self.text


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
