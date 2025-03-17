Features
🔹 User Authentication
Sign Up: Users can register by providing necessary details.
Login/Logout: Secure authentication system for registered users.
🔹 Student Registration
Users can enter data for up to 10 students, and the details will be stored in the database.
Upon successful registration, an email confirmation will be sent to the registered student, notifying them of their successful registration.
🔹 Dashboard (After Login)
Once logged in, users will have access to the following sections:

📌 My Profile
Displays user details, including their profile image and the information provided during registration.
Users can update their profile details, including their profile picture.
Admins can also update user profiles as needed.
📌 Display Data
Displays all registered student details in a tabular format using Bootstrap for a clean and responsive UI.
📌 Technology Stack
Django (Python framework for backend development)
Bootstrap (for responsive front-end design)
SQLite / PostgreSQL (for database management)
Django Authentication System (for secure login/logout)
Django Email Backend (for sending registration confirmation emails)
📌 Installation & Setup
Clone the repository:
bash
Copy
Edit
git clone <repository_url>
cd <project_directory>
Create a virtual environment and install dependencies:
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Apply database migrations:
bash
Copy
Edit
python manage.py migrate
Run the development server:
bash
Copy
Edit
python manage.py runserver
Open your browser and navigate to:
cpp
Copy
Edit
http://127.0.0.1:8000/
