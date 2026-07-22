# Funções sendo testadas
from app import filtrar_alertas


# Testes que devem retornar True
def test_alerta_nohardhat():
    alert = {"alert_type": "NoHardHat"}
    assert filtrar_alertas(alert) is True


def test_alerta_redzone():
    alert = {"alert_type": "RedZoneIntrusion"}
    assert filtrar_alertas(alert) is True


# Testes que devem retornar False
def test_alerta_outroA():
    alert = {"alert_type": "NoGloves"}
    assert filtrar_alertas(alert) is False


def test_alerta_outroB():
    alert = {"alert_type": "NoGlasses"}
    assert filtrar_alertas(alert) is False
