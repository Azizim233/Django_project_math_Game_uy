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


بۇ پروجكىت بەقەت تېلىفون ئارقىلىقلا نورمال ئىشلەيدۇ

