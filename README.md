🧰 Project Setup & Dependencies
This project uses a virtual environment (.venv) to isolate dependencies and ensure compatibility across systems.
Follow these steps to set up and run the project:
⚙️ 1. Requirements
Python 3.10 or newer
pip (Python package manager)
Git (optional, if cloning from GitHub)
📦 2. Create a Virtual Environment
Create a local virtual environment inside your project folder.
🪟 Windows (PowerShell / CMD):
python -m venv .venv
.venv\Scripts\activate
🍎 macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
✅ After activation, your terminal prompt should display:
(.venv)
This means all installations will now be contained inside .venv.
📦 3. Install Dependencies
With your .venv active, install all the required libraries:
pip install flask flask_sqlalchemy
These will automatically pull in all sub-dependencies:
Flask — Web framework
Flask-SQLAlchemy — Database ORM
Werkzeug — Security and hashing utilities
Jinja2 — HTML templating engine
MarkupSafe, itsdangerous, click — Internal Flask dependencies
📄 4. Save Dependencies
Once installed, freeze them into a requirements.txt file so the environment can be recreated anywhere:
pip freeze > requirements.txt
Your requirements.txt will look similar to:
click==8.x.x
Flask==3.x.x
Flask-SQLAlchemy==3.x.x
itsdangerous==2.x.x
Jinja2==3.x.x
MarkupSafe==2.x.x
Werkzeug==3.x.x
🔄 5. Recreate Environment (for other machines)
If you clone this project or move to another computer, run:
🪟 Windows:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
🍎 macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
✅ This installs all dependencies exactly as the original environment.
🧠 6. Useful Commands
Action	Command
Check Python version	python --version
Check installed packages	pip list
Update pip	python -m pip install --upgrade pip
Deactivate environment	deactivate
Reinstall dependencies from file	pip install -r requirements.txt
🚫 7. Add .venv to .gitignore
Never upload your virtual environment to GitHub — it’s large and system-specific.
In your .gitignore, make sure you have:
.venv/
venv/
__pycache__/
*.pyc
🧱 8. Run the App
After the setup, you can start your Flask application with:
python app.py
Then open your browser at:
http://127.0.0.1:5000
✅ Final Checklist
✔ Virtual environment created
✔ Dependencies installed locally
✔ requirements.txt generated
✔ .venv excluded from Git
✔ App runs successfully with python app.py
