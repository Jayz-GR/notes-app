\# Notes App



A simple Flask web app to create, edit, and delete personal notes.  

Originally built using a JSON file for storage, now upgraded to use \*\*SQLite\*\* for more reliable data management.



\## ✨ Features

\- Add new notes

\- Edit existing notes

\- Delete notes

\- Persistent storage with SQLite database



\## 🛠️ Tech Stack

\- Python 3

\- Flask

\- Flask-SQLAlchemy

\- HTML / CSS



\## 🚀 Setup



1\. Clone the repository using cmd/terminal



&nbsp;	git clone https://github.com/Jayz-GR/notes-app.git

&nbsp;	cd notes-app



2\. Create a virtual environment (recommended)



&nbsp;	python -m venv venv

&nbsp;	source venv/bin/activate      # macOS/Linux

&nbsp;	venv\\Scripts\\activate         # Windows



3\. Install dependencies



&nbsp;	pip install -r requirements.txt



4\. Run the app



&nbsp;	python app.py



Visit http://127.0.0.1:5000/ in your browser.



\## 🗂️ Project Structure



notes\_app/

├─ app.py

├─ requirements.txt

├─ templates/

│  ├─ index.html

│  └─ edit.html

└─ static/

&nbsp;  └─ style.css



!\[Notes App Screenshot](Screenshot.png)





