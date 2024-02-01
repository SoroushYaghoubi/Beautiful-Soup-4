class Lawyer:
    # getters and setters

    @property
    def web_page(self):
        return self.web_page

    @property
    def name(self):
        return self.name

    @property
    def expl(self):
        return self.expl

    @property
    def addr(self):
        return self.addr

    @property
    def telefon(self):
        return self.telefon

    @web_page.setter
    def web_page(self, value):
        self.web_page = value

    @name.setter
    def name(self, value):
        self.name = value

    @expl.setter
    def expl(self, value):
        self.expl = value

    @addr.setter
    def addr(self, value):
        self.addr = value

    @telefon.setter
    def telefon(self, value):
        self.telefon = value