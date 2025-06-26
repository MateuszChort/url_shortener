import string, random
from .models import ShortURL


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    # Ensure unique code
    for _ in range(10):
        code = "".join(random.choices(chars, k=length))
        if not ShortURL.objects.filter(short_code=code).exists():
            return code
    raise Exception("Could not generate unique short code after 10 attempts.")


def create_short_url(original_url):
    obj, created = ShortURL.objects.get_or_create(original_url=original_url)
    if created:
        obj.short_code = generate_code()
        obj.save()
    return obj
