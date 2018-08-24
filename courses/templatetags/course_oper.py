from django import template

register = template.Library()

# TODO: i think i can delete this
#@register.filter
#def sub(value, arg):
#    return value - arg

@register.simple_tag
def convert_text(value):
    str_val = str(value)
    year = str_val[:4]
    qtr = int(str_val[4])
    if qtr == 4:
        return "Autumn " + year
    elif qtr == 1:
        return "Winter " + year
    elif qtr == 2:
        return "Spring " + year
    else:
        return "Summer " + year
