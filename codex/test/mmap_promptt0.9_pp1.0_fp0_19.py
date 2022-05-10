import mmap
# Test mmap.mmap
def save_html_to_file(slug_list, filename):
    n = len(slug_list)
    step = 1000
    start = 0
    with open(filename, 'w+') as f:
        for i in range(n // step):
            for slug in slug_list[start:i * step]:
                response = requests.get(url.format(slug))
                if response.status_code == 200:
                    f.write(response.text + "\n")
                else:
                    print("Error: " + slug)
            
            start = i * step
    
    for slug in slug_list[start:]:
        response = requests.get(url.format(slug))
        if response.status_code == 200:
            f.write(response.text + "\n")
        else:
            print("Error: " + slug)
    return

if __name__ == "__main__":
    print("Begin")
    for team_slug in team_list:
        print(team_slug)
