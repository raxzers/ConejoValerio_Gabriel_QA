CORREO = "man@mail.com"
PASSWORD_VALIDA = "Segura123"
PASSWORD_INCORRECTA = "Incorrecta999"

TITULO_ESPERADO = "Bienvenido"
MENSAJE_ERROR_ESPERADO = "Correo o contraseña incorrectos"  # ajustar al texto real de la app


def test_inicio_de_sesion_exitoso_muestra_titulo_bienvenido(login_page):
    login_page.iniciar_sesion(CORREO, PASSWORD_VALIDA)

    assert login_page.obtener_titulo_home() == TITULO_ESPERADO


def test_inicio_de_sesion_con_password_incorrecta_muestra_mensaje_de_error(login_page):
    login_page.iniciar_sesion(CORREO, PASSWORD_INCORRECTA)

    assert login_page.obtener_mensaje_error() == MENSAJE_ERROR_ESPERADO