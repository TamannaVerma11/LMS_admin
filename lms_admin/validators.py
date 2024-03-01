from django.core.exceptions import ValidationError

def verifiy_first_name(value):
    raise ValidationError('Please add valid name')