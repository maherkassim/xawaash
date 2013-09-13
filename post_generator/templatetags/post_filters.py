from django import template

register = template.Library()

@register.filter(name='get_val')
def get_val(dictionary, key):
    # Retrieves value in dictionary for the given key
    return dictionary.get(key)