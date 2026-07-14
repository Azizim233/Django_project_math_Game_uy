math_game/
│
├── game/
│   ├── templates/game/index.html   # Mobile-Optimized Tailwind UI Template
│   ├── middleware.py               # Device User-Agent interceptor
│   ├── views.py                    # Game logic, dynamic scaling engine
│   └── urls.py                     # App endpoints
│
├── screenshots/
│   └── gameplay_flow.png           # Bounded workflow screenshot
│
├── math_game/
│   └── settings.py                 # Middleware stack config & integration
└── manage.py


قاچىلاش تەلەپ قىلىنىدۇ
pip install django-user-agents

تەلەپ قىلىنىدۇ
python manage.py migrate

ئاخىرىدا 
python3 manage.py runserver

توركۆرگۈچتە تۆۋەندىكى ئادرىسنى ئېچىڭ

http://127.0.0.1:8000/
<img width="222" height="279" alt="Screenshot 2026-07-14 at 12 35 45" src="https://github.com/user-attachments/assets/1a76f122-39d6-461c-b4b4-8551489341d7" />


بۇ پروجكىت بەقەت تېلىفون ئارقىلىقلا نورمال ئىشلەيدۇ

