from django.db import models
from django.urls import reverse
import django.utils.timezone

# TOD is short for Time of Day
TOD = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
)

tracking = (
    ('L', 'Location'),
    ('F', 'Flight Patterns'),
    ('N', 'Nesting Habits'),
)

class Tag(models.Model):
    color = models.CharField(max_length=50)
    tracking = models.CharField(max_length=1, choices=tracking, default=tracking[0][0])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age= models.IntegerField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
    
class Sighting(models.Model):
    date = models.DateField('sighting date', default=django.utils.timezone.now)
    location = models.CharField(max_length=100)
    tod = models.CharField(max_length=1, choices=TOD, default=TOD[0][0])

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_tod_display()} on {self.date} for {self.finch}"