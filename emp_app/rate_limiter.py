from collections import defaultdict, deque
from django.http import JsonResponse
import time

rate_limit_store = defaultdict(deque)

RATE_LIMIT = 10     
TIME_WINDOW = 60        

def is_allowed(client_ip: str) -> bool:
    now = time.time()
    window = rate_limit_store[client_ip]

  
    while window and window[0] <= now - TIME_WINDOW:
        window.popleft()

    if len(window) < RATE_LIMIT:
        window.append(now)
        return True
    return False

def rate_limit(view_func):
    def wrapped_view(request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR', 'unknown')
        org = request.GET.get('org_id', 'default')
        client_ip = f"{ip}-{org}"

        if not is_allowed(client_ip):
            return JsonResponse(
                {"error": "Rate limit exceeded. Try again later."},
                status=429
            )

        return view_func(request, *args, **kwargs)
    return wrapped_view
