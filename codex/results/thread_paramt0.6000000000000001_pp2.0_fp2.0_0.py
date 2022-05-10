import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, range(100000000, 1, -1))))).start()



# Подстановка по шаблону

def make_substituter(template):
    def substituter(replacements):
        def substitute(match):
            return replacements[match.group(1)]
        return re.sub(r'\$\{([^\}]+)\}', substitute, template)
    return substituter

substitute = make_substituter('The ${animal} is ${action}.')
print(substitute({'animal': 'cat', 'action': 'sleeping'}))



# Пример использования замыкания в качестве промежуточного кода

def make_counter(initial=0, step
