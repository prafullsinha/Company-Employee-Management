# do : Create a Django Web App called “Profile Storer” where a company can sign up using Email.

Once signed up, he can add more people to his team. Every team member can be either “Normal” type or “Manager” type. When you add a team member, that particular person gets an email with password, which he/she can use to login.

When a Manager type user logs in, he sees a list of all users of that company, he can go and edit any of the profile.

When a Normal user logs in, he sees only his own profile that he can edit.

Questions in Profile:
Name, Phone, Gender, Hobbies, Profile Picture.

#pip freeze
Django==2.2.5
django-crispy-forms==1.7.2
django-extensions==2.2.1
django-use-email-as-username==1.0.2
Pillow==6.2.1
pkg-resources==0.0.0
psycopg2==2.8.3
pytz==2019.2
six==1.12.0
sqlparse==0.3.0

