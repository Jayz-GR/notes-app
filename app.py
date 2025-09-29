from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_note = Note(content=request.form['note'])
        db.session.add(new_note)
        db.session.commit()
        return redirect('/')
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/delete/<int:index>')
def delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(id):
        note = Note.query.get_or_404(id)
        if request.method == 'POST':
             note.content = request.form['note']
             db.session.commit()
             return redirect('/')
        return render_template('edit.html', note=note.content)

if __name__ == '__main__':
    app.run(debug=True)