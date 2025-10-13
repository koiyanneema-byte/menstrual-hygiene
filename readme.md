# Menstrual Hygiene Survey — My Voice for Hygiene

This Django-powered website is designed to amplify learner voices around menstrual hygiene. It provides a safe, anonymous space for students to share their challenges, ideas, and feedback — helping educators, guardians, and advocates understand real needs. The platform supports CBC-aligned classroom integration, youth-led research, and digital literacy through ethical data collection and storytelling.
Built to empower Neema’s advocacy mission, My Voice for Hygiene blends technology, empathy, and education — turning personal experiences into collective action.


---

## Features

-  Bootstrap-styled survey form
-  Saves responses to a database
- CSRF-protected form submission
- Admin panel for viewing submissions
- Ready for deployment with Gunicorn

---

## 📦 Requirements

Your `requirements.txt` should include:


---

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/koiyanneema-byte/hygieneform.git
cd hygieneform

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

#Apply database migrations
python manage.py makemigrations
python manage.py migrate

#finnally launch it via cmd
python manage.py runserver

