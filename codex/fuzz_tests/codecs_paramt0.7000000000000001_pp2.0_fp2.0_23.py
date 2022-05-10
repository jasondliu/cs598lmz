import codecs
codecs.register_error('surrogate_or_special', codecs.surrogateescape)

def get_parsed_response(response, include_attributes=False):
    
    if isinstance(response, dict):
        response = json.dumps(response)
    
    parsed_response = dict()
    root = ET.fromstring(response)
    items = root.getchildren()
    for item in items:
        for subitem in item.getchildren():
            if subitem.tag == "Data":
                data = dict()
                for data_item in subitem.getchildren():
                    data[data_item.tag] = data_item.text
                parsed_response[item.tag] = data
                
            elif subitem.tag == "Attribute":
                if include_attributes:
                    attribute = subitem.find("Name").text
                    value = subitem.find("Value").text
                    parsed_response[attribute] = value

            else:
                parsed_response[subitem.tag] = subitem.text

    return parsed_response


class SpatialReference:

