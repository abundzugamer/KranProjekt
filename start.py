import Controll as controll
import logger
from UI.KranUI import KranApp

KranApp().run()
x = logger.Logger()
y = controll.Controll("COM16", x)
KranApp().KranUI().con = y