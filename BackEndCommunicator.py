import numpy


# back end side
# called from GUI side this fn should be in backend
# more fn will or might be added
def check_user_auth(id: str, passwd: str) -> None: ...


def auth_qrcode_request() -> None: ...


def change_applicator_value(value_list:list) -> None:...


# GUI side
# called from backend
class BackEndCommunicator:
    """for loading screen"""

    def gui_loading_start(self) -> None: ...
    def gui_loading_update(self, progress: int) -> None: ...
    def gui_loading_finish(self) -> None: ...

    """for login screen"""

    def auth_result(self, result: bool, message: str) -> None: ...
    def auth_qrcode_request(self) -> None: ...
    def auth_qrcode_received(self, qrcode_image: numpy.ndarray) -> None:  ...

    """for Scan auth ... screen"""

    def auth_complete(self) -> None: ...
    def chking_qrcode_request(self) -> None: ...
    def chking_qrcode_received(self, qrcode:numpy.ndarray) -> None: ...

    """for scan screen2"""
    def checking_complete(self) -> None: ...

