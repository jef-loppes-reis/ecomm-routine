"""--- Constantes ---"""

from typing import Dict, List, Any

ULTIMO_HORARIO_COMERCIAL: int = 19
HORARIO_INICIAL_COMERCIAL: int = 7
ULTIMO_HORARIO_SABADO: int = 16

HORARIO_COMERCIAL: List[int|float] = list(range(HORARIO_INICIAL_COMERCIAL, ULTIMO_HORARIO_COMERCIAL))
HORARIO_COMERCIAL_SABADO: List[int|float] = list(range(HORARIO_INICIAL_COMERCIAL, ULTIMO_HORARIO_SABADO))

DIAS_SEMANA: List[Dict[int, str]] = [
    {0: "Segunda-feira"},
    {1: "Terça-feira"},
    {2: "Quarta-feira"},
    {3: "Quinta-feira"},
    {4: "Sexta-feira"},
    {5: "Sábado"},
    {6: "Domingo"},
]

PROJECTS: Dict[str, List[Dict[str, Any]]] = {
    "update_price_storage_ml": [
        {
            "name_module": "main.py",
            "path": "../update_price_storage_ml",
            "hour": HORARIO_COMERCIAL[3:],
            "days": [list(dia.values())[0] for dia in DIAS_SEMANA if 6 not in dia.keys()],
            "hour_specific": list(range(10, 16)),
        }
    ],
    "update_price_stock_shopee": [
        {
            "name_module": "main.py",
            "path": "../update_price_stock_shopee",
            "hour": HORARIO_COMERCIAL[3:],
            "days": [list(dia.values())[0] for dia in DIAS_SEMANA if 6 not in dia.keys()],
            "hour_specific": list(range(10, 16)),
        }
    ],
    "db_ecomm": [
        {
            "name_module": "main.py --truncate",
            "path": "../db_ecomm",
            "hour": [],
            "days": [list(dia.values())[0] for dia in DIAS_SEMANA],
            "hour_specific": list(range(7)),
        }
    ],
    "update_cfop": [
        {
            "name_module": "update.py",
            "path": "../new-ml-dre/data",
            "hour": HORARIO_COMERCIAL,
            "days": [list(dia.values())[0] for dia in DIAS_SEMANA],
            "hour_specific": [],
        }
    ]
}
