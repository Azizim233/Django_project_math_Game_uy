# game/middleware.py
from django.http import HttpResponseForbidden

class MobileOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ئەگەر تېلېفون ياكى تاختا كومپيۇتېر بولمىسا، كىرىشنى رەت قىلىدۇ
        if not (request.user_agent.is_mobile or request.user_agent.is_tablet):
            return HttpResponseForbidden(
                "<h1>كەچۈرۈڭ!</h1><p>بۇ ئويۇن پەقەت تېلېفوندىلا ئىشلەيدۇ. تېلېفونىڭىز ئارقىلىق كىرىڭ.</p>",
                content_type="text/html; charset=utf-8"
            )
        return self.get_response(request)