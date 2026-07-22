def filtrar_alertas(alert):
    filtros = {"NoHardHat", "RedZoneIntrusion", "NoGloves"}
    return alert.get("alert_type") in filtros
# Aqui neste programa ele deverá filtrar apenas os itens solicitados pela empresa com base nos alertas feitos e declarados na função deste arquivo e na outra.