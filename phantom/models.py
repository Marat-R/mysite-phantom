import os
import random
from django.db import models
from django.shortcuts import reverse
from phantom.utils import unique_slug_generator
from django.dispatch import receiver
from django.db.models.signals import pre_save



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 399999999)
    name, ext = get_filename_ext(filename)
    final_name = f'{new_filename}{ext}'
    return f'product_images/{new_filename}/{final_name}'


class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created_at', )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("phantom:ad_detail", kwargs={"slug": self.slug})


class AdvertisementImage(models.Model):
    image = models.ImageField(upload_to=upload_image_path)
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.CASCADE, related_name="images"
        ) 
    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'

    def __str__(self):
        return f'{self.advertisement.title}.jpg'


class ContactData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Advertisement)
def advertisement_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)