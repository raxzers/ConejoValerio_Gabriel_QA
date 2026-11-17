from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Page Object de la pantalla de inicio de sesión."""

    # Locators (accessibility id)
    EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input_email")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input_password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "btn_login")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "txt_error")
    HOME_TITLE = (AppiumBy.ACCESSIBILITY_ID, "home_title")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- helpers internos ----------

    def _esperar_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _esperar_clickeable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ---------- acciones de la pantalla ----------

    def ingresar_correo(self, correo: str) -> None:
        campo = self._esperar_visible(self.EMAIL_INPUT)
        campo.clear()
        campo.send_keys(correo)

    def ingresar_password(self, password: str) -> None:
        campo = self._esperar_visible(self.PASSWORD_INPUT)
        campo.clear()
        campo.send_keys(password)

    def presionar_iniciar_sesion(self) -> None:
        self._esperar_clickeable(self.LOGIN_BUTTON).click()

    def iniciar_sesion(self, correo: str, password: str) -> None:
        """Flujo completo: llena los campos y presiona el botón."""
        self.ingresar_correo(correo)
        self.ingresar_password(password)
        self.presionar_iniciar_sesion()

    # ---------- lecturas para las aserciones ----------

    def obtener_titulo_home(self) -> str:
        return self._esperar_visible(self.HOME_TITLE).text

    def obtener_mensaje_error(self) -> str:
        return self._esperar_visible(self.ERROR_MESSAGE).text