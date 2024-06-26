from django.db import models

class User(models.Model):
    Username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, unique=True)


    class Meta:
        db_table = "User_table"

class PropertyInformation(models.Model):
    PROPERTY_TYPES = (
        ('land', 'Land'),
        ('home', 'Home'),
    )

    property_type = models.CharField(max_length=5, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_property_type_display()} - {self.location}"