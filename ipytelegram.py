import telepot
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic


@magics_class
class TelegramMagics(Magics):

    def __init__(self, shell):
        super(TelegramMagics, self).__init__(shell)
        self.token = None
        self.user_id = None
        self.bot = None

    @line_magic
    def telegram_setup(self, line):
        r = line.strip().split()
        if len(r) == 2:
            self.token, self.user_id = r
            self.bot = telepot.Bot(self.token)
        else:
            raise ValueError

    @cell_magic
    def telegram_send(self, line, cell):
        self.shell.run_cell(cell)
        self.bot.sendMessage(self.user_id, line)


def load_ipython_extension(ipython):
    magics = TelegramMagics(ipython)
    ipython.register_magics(magics)


def unload_ipython_extension(ipython):
    pass
