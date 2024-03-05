from config import DevelopmentConfig

from flask import Flask, redirect, render_template, request, url_for
from flask import flash
from flask import g
from flask_wtf.csrf import CSRFProtect
import forms
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def main():
    return render_template("layout.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    create_form = forms.UserForm(request.form)
    
    if request.method == "POST":
        alumnos = Alumnos(
            nombre = create_form.nombre.data,
            primerApellido = create_form.primerApellido.data,
            segundoApellido = create_form.segundoApellido.data,
            correo = create_form.correo.data
        )
        db.session.add(alumnos)
        db.session.commit()
        return redirect('/ABC_Completo')
    
    return render_template('index.html', form=create_form)

@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCompleto() :
    form_alumno = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", alumnos = alumnos)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()
    
@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumno.nombre
        create_form.primerApellido.data = alumno.primerApellido
        create_form.correo.data = alumno.correo
        
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        
        # DELETE FROM alumnos where id = id
        db.session.delete(alum)
        db.session.commit()
        
        return redirect(url_for('ABCompleto'))

    return render_template('eliminar.html', form = create_form)