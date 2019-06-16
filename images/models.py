from django.db import models

from django.utils.text import slugify

from django.utils.timezone import now

# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name[:20])
            self.created = now()
        self.updated = now()
        super(Common, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created', )
        abstract = True


class Vehicle(Common):
    description = models.TextField(blank=True)


class Image(Common):
    image = models.FileField(upload_to="images/%Y/%m/%d")
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="images"
    )