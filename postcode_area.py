import re

def postcode_area(postcode):
    return re.search(r'^.*?(?=[0-9])', postcode).group(0)