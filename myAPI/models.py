from django.db import models

# Create your models here.


class exited(models.Model):
    Geography_choices= (
        ('France', 'France'),
        ('Germany', 'Germany'),
        ('Spain', 'Spain')
    )   
    Gender_choices= (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Tenure_choices= (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    NumOfProducts_choices= (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    )
    HasCrCard_choices= (
        ('1', 'Yes'),
        ('0', 'No')
    )
    IsActiveMember_choices= (
        ('1', 'Yes'),
        ('0', 'No')
    )

    
    CreditScore=models.IntegerField(default=0)
    Geography=models.CharField(max_length=12, choices= Geography_choices)
    Gender=models.CharField(max_length=10, choices = Gender_choices)
    Age=models.IntegerField(default=0)
    Tenure=models.IntegerField(choices= Tenure_choices)
    Balance=models.IntegerField(default=0)
    NumOfProducts=models.IntegerField(choices= NumOfProducts_choices)
    HasCrCard=models.CharField(max_length=12, choices= HasCrCard_choices)
    IsActiveMember=models.CharField(max_length=12, choices= IsActiveMember_choices)
    EstimatedSalary=models.IntegerField(default=0)

