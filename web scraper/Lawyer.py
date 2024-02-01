class Lawyer:
    def __init__(self):
        self._web_page = None
        self._name = None
        self._expl = None
        self._telefon = None

    @property
    def web_page(self):
        return self._web_page

    @property
    def name(self):
        return self._name

    @property
    def expl(self):
        return self._expl

    @property
    def telefon(self):
        return self._telefon

    @web_page.setter
    def web_page(self, value):
        self._web_page = value

    @name.setter
    def name(self, value):
        self._name = value

    @expl.setter
    def expl(self, value):
        self._expl = value

    @telefon.setter
    def telefon(self, value):
        self._telefon = value

    def __str__(self):
        e = ""
        if self.name:
            e += self._name + "\n"
        else:
            e += "!name!\n"

        if self.web_page:
            e += self._web_page + "\n"
        else:
            e += "!web page!\n"

        if self.expl:
            e += self._expl + "\n"
        else:
            e += "!expl!\n"

        if self.telefon:
            e += f"{self._telefon}\n"
        else:
            e += "!telefon!\n"

        return e
