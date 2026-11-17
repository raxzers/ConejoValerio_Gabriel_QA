import pytest

from shopgo.validaciones import calcular_envio, validar_password



# ---------- validar_password: valores límite de longitud ----------

@pytest.mark.parametrize(
    "password, esperado",
    [
        ("Qwe1234", False),            # 7 caracteres: uno menos del mínimo
        ("Asd12345", True),            # 8 caracteres: mínimo válido
        ("A" + "j" * 18 + "1", True),  # 20 caracteres: máximo válido
        ("A" + "h" * 19 + "1", False),  # 21 caracteres: uno más del máximo
    ],
    ids=[
        "7_caracteres_es_invalida",
        "8_caracteres_es_valida",
        "20_caracteres_es_valida",
        "21_caracteres_es_invalida",
    ],
)
def test_password_valida_limites_de_longitud(password, esperado):
    assert len(password) in (7, 8, 20, 21)  # protege contra errores al armar los casos
    assert validar_password(password) is esperado


# ---------- validar_password: casos negativos ----------

@pytest.mark.parametrize(
    "password",
    [
        "abcdefg1",   # sin mayúscula
        "zxcvbnmlkj1",
    ],
    ids=["sin_mayuscula_8_caracteres", "sin_mayuscula_11_caracteres"],
)
def test_password_sin_mayuscula_es_invalida(password):
    assert validar_password(password) is False


@pytest.mark.parametrize(
    "password",
    ["Abcdehjk", "ABCDEHJKIJ"],
    ids=["sin_numero_solo_letras", "sin_numero_todo_mayusculas"],
)
def test_password_sin_numero_es_invalida(password):
    assert validar_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "ERT 1234",    # espacio en medio
        " Ert12345",   # espacio al inicio
        "Abc12657 ",   # espacio al final
        "Abc\t12895",  # tabulador
    ],
    ids=[
        "espacio_en_medio_es_invalida",
        "espacio_al_inicio_es_invalida",
        "espacio_al_final_es_invalida",
        "tabulador_es_invalida",
    ],
)
def test_password_con_espacios_es_invalida(password):
    assert validar_password(password) is False


def test_password_texto_vacio_es_invalida():
    assert validar_password("") is False


def test_password_none_es_invalida():
    assert validar_password(None) is False


def test_password_que_cumple_todas_las_reglas_es_valida():
    assert validar_password("Segura123") is True


# ---------- calcular_envio: valores límite ----------

@pytest.mark.parametrize(
    "subtotal, esperado",
    [
        (24999, 2500),   # justo debajo del umbral: paga envío
        (25000, 0),      # en el umbral: envío gratis
        (25001, 0),      # sobre el umbral: envío gratis
        (0, 2500),       # subtotal cero: paga envío
    ],
    ids=[
        "24999_cobra_envio_2500",
        "25000_envio_gratis",
        "25001_envio_gratis",
        "subtotal_cero_cobra_envio_2500",
    ],
)
def test_envio_segun_subtotal(subtotal, esperado):
    assert calcular_envio(subtotal) == esperado


def test_envio_con_decimales_justo_bajo_el_umbral_cobra_envio():
    assert calcular_envio(24999.99) == 2500


# ---------- calcular_envio: subtotal negativo ----------

def test_envio_con_subtotal_negativo_lanza_value_error():
    with pytest.raises(ValueError, match="subtotal negativo"):
        calcular_envio(-1)