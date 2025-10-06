from django import template

register = template.Library()

censor_list = ['редиск', 'перфекционизм', 'огур']

@register.filter(name="censor")
def censor(text: str) -> str:
    if not isinstance(text, str):
        return text

    for word in censor_list:
        text = text.replace(word[1:], '*' * len(word[1:]))
    return text
