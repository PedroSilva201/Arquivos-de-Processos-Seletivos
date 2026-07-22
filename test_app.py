# Caso de teste fornecido
alert = {
    "timestamp": "1651347332",
    "alert_type": "NoGloves",
    "src_cam": "PETR_CAM01",
    "bounding_box": [(100, 200), (150, 250)],
    "alert_confidence": 0.85
}

# Lista de alertas que queremos filtrar
filters = ["NoHardHat", "RedZoneIntrusion"]

# Pega o alert_type do dicionário
alert_type = alert["alert_type"]

# Verifica se o alert_type está dentro dos filtros
is_allowed = alert_type in filters

# Imprime o resultado no terminal
print(f"Alert type: {alert_type}")
print(f"Está dentro dos filtros? {is_allowed}")
