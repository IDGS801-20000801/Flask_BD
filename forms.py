from wtforms import validators
from wtforms import IntegerField, StringField, EmailField
from wtforms import Form


class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField(
        'nombre',
        [
            validators.DataRequired(message='El nombre es requerido'),
            validators.length(min= 4, max=15, message='Ingresa un nombre valido')
        ]
    )
    primerApellido = StringField(
        'primer apellido',
        [
            validators.DataRequired(message='el primer apellido es requerido'),
            validators.length(min=4, max=20, message='Ingresa un apellido valido')
        ]
    )
    segundoApellido = StringField('segundo apellido')
    correo = EmailField(
        'correo',
        [
            validators.DataRequired(message="El correo es requerido"),
            validators.email('Ingresa un correo valido')
        ]
    )