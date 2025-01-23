from core.extension.extension import Extension
from can20_app import CAN20App


def init_app(app: CAN20App):
    code_based_extension.init()


code_based_extension = Extension()
