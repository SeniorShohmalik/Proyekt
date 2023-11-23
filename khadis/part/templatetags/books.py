from django import template
from re import IGNORECASE, compile, escape as rescape
from django.utils.safestring import mark_safe
import re
register = template.Library()


@register.filter()
def highlight_yellow(text, value):
    if text is not None:
        text = str(text)
        src_str = re.compile(value, re.IGNORECASE)
        str_replaced = src_str.sub(f"<span class=\"highlight\">{value}</span>", text)
    else:
        str_replaced = ''

    return mark_safe(str_replaced)