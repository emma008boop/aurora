import re


def text_processing_mvr(raw_text: str) -> dict:
    # 1. Limpieza inicial: colapsar múltiples espacios y saltos de línea en espacios simples
    text = re.sub(r"\s+", " ", raw_text)

    # 2. Definición de patrones de expresiones regulares (Regex)
    name_pattern = r"Full\s+Name:\s*(.*?)(?=\s*●|\n|$)"
    dob_pattern = r"Date\s+of\s+Birth:\s*([\d/]+)"
    cld_pattern = r"Driver\s+License\s+Number:\s*([A-Za-z0-9-]+)"
    points_pattern = r"Total\s+Points\s+\(3-Year\s+History\):\s*(\d+)"
    issue_date_pattern = r"Original\s+Issue\s+Date:\s*([\d/]+)"
    expiration_date_pattern = r"Expiration\s+Date:\s*([\d/]+)"
    violation_code_pattern = r"Violation\s+Code:\s*([A-Za-z0-9\s-]+?)(?=\s*●|\n|$)"

    # 3. Búsqueda de datos únicos (esperamos solo una coincidencia por documento)
    name = re.search(name_pattern, text)
    dob = re.search(dob_pattern, text)
    cld = re.search(cld_pattern, text)
    points = re.search(points_pattern, text)
    issue_date = re.search(issue_date_pattern, text)
    expiration_date = re.search(expiration_date_pattern, text)

    # 4. Búsqueda de datos múltiples (captura TODOS los códigos de violación existentes)
    raw_violation_codes = re.findall(violation_code_pattern, text)
    # Limpiamos los espacios en blanco de cada código encontrado usando comprensión de listas
    violation_codes = [code.strip() for code in raw_violation_codes]

    # Conteo total de bloques de violación basados en la etiqueta "Violation Date:"
    total_violations = text.count("Violation Date:")

    # 5. Construcción del perfil del conductor estructurado en un diccionario
    driver_profile = {
        "name": name.group(1).strip() if name else "UNKNOWN",
        "dob": dob.group(1).strip() if dob else None,
        "cld": cld.group(1).strip() if cld else "UNKNOWN",
        "mvr_points": points.group(1).strip() if points else 0,
        "issue_date": issue_date.group(1).strip() if issue_date else None,
        "expiration_date": (
            expiration_date.group(1).strip() if expiration_date else None
        ),
        "violations_count": total_violations,
        "violation_codes": violation_codes,  # Devuelve una lista de strings: ['VC 22350', ...]
    }

    return driver_profile
