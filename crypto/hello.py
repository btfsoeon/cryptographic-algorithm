msg = 'hello'
print(msg)

sayHello = {
    'Ko': 'Anyeong',
    'Ja': 'Konichiwa',
    'En': 'Hello',
}

class Hello:
    def __init__(self, lang):
        self._lang = lang
    
    def __str__(self):
        return f'lang : {self._lang}'

    def say(self):
        return sayHello[self._lang]
