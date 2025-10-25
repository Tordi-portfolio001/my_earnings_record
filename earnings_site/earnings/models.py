from django.db import models

class Earning(models.Model):
    job_name = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='earnings_images/')
    image2 = models.ImageField(upload_to='earnings_images/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.job_name
