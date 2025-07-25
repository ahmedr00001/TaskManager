# chat/templatetags/chat_extras.py
from django import template

register = template.Library()

@register.filter
def dictkey(d, key):
    return d.get(key)