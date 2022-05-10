import lzma
lzma.LZMAError
cj_map_name2city = json.load(open('city_jinpai_map.json', 'r'))
cj_map_city2name = {}
for k, v in cj_map_name2city.items():
    cj_map_city2name[v] = k

def get_name(city, region):
    if city and region:
        if city in cj_map_city2name.keys():
            return cj_map_city2name[city]
        else:
            province_regions_map = json.load(open('province_region_name.json', 'r'))
            try:
                regions = province_regions_map[city]
                if region in regions and region + '市' in cj_map_city2name.keys():
                    return cj_map_city2name[region + '市']
                else:
                    return city
            except:
                return city
    else:
        return city

def get_names(city, region):
   
