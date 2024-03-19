class Locators:
    """
        Class that contains the paths of automation
    """
    def __init__(self):
        """
            Dados iniciais
        """
        self.dados = 'Dados'


class Controller:
    """
        class made for controll the automation
    """
    def __init__(self):
        """
            Dados Iniciais
        """
        self.locators = Locators()
        print("ola")

    def dados(self):
        """
            Printando dados iniciais
        """
        print(self.locators.dados)

    def teste(self):
        """
            printando
        """
        print("apenas um teste")

run = Controller()
run.teste()
