from django.db import models

# Create your models here
class User_Details(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    points = models.IntegerField()    

#     def __str__(self):
#         return self.name

# class User_History(models.Model):
#     name = models.ForeignKey(User_Details, on_delete=models.CASCADE)
#     date = models.DateField()
#     food_emsn = models.IntegerField()
#     travel_emsn= models.IntegerField()
#     energy_emission = models.IntegerField()
#     daily_emsn = models.IntegerField()

#     def __str__ (self):
#         return self.name
    
# class User_Goal(models.Model):
#     name = models.ForeignKey(User_Details, on_delete=models.CASCADE)
#     gl_travel_emsn = models.IntegerField()
#     gl_energy_emsn = models.IntegerField()
#     gl_food_emsn = models.IntegerField()
#     gl_daily_emsn = models.IntegerField()

#     def __str__ (self):
#         return self.name

