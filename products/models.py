from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='in Indian Rupee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created_at.strftime('%d/%m/%Y')}"