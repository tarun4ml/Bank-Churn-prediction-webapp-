from django import forms

class ExitedForm(forms.Form):
    CreditScore = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Enter Credit score(350 - 850)'}), label=('Credit Score'))
    Geography = forms.ChoiceField(choices= [('France', 'France'),('Germany', 'Germany'),('Spain', 'Spain')])
    Gender = forms.ChoiceField(choices = [('Male', 'Male'),('Female', 'Female')])
    Age = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Enter Age(18-90)'}))
    Tenure = forms.ChoiceField(choices= [(0, 0),(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)])
    Balance = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Balance amount(<250000)'}), label='Balance amount')
    NumOfProducts = forms.ChoiceField(choices= [(1, 1),(2, 2),(3, 3),(4, 4)], label='Number of product(s)')
    HasCrCard = forms.ChoiceField(choices= [(1, 'Yes'),(0, 'No')], widget= forms.RadioSelect, initial='1', label='Has Credit Card?')
    IsActiveMember = forms.ChoiceField(choices= [(1, 'Yes'),(0, 'No')], widget= forms.RadioSelect, initial='1', label='Is Active Member?')
    EstimatedSalary = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Estimated Salary(<200000)'}), label='Estimated Salary')

    
