from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date():
    return datetime.now().strftime('%Y-%m-%d')


@register.simple_tag
def truncate_text(text, length=50):
    if len(text) > length:
        return text[:length] + "..."
    return text

@register.inclusion_tag('user_list.html')
def show_users(users):
    return {'users': users}
