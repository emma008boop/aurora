import re


def loss_run_parser(raw_text: str) -> dict:
    """
    It takes text extracted from a Loss Run PDF and returns a
    structured dictionary containing general information and claims.
    """
    texto = re.sub(r"\s+", " ", raw_text)

    patron_insured = r"Insured\s+Name:\s*\"([^\"]+)\""
    patron_policy = r"Policy\s+Number:\s*\"([^\"]+)\""
    patron_carrier = r"Carrier:\s*.*?([A-Za-z\s]+Insurance\s+Corp\.)"
    patron_total_claims = r"TOTAL\s+Claims\s+(\d+)"
    patron_total_incurred = r"TOTAL\s+INCURRED\s+\$([\d,]+)"

    datos_reporte = {
        "insured_name": None,
        "policy_number": None,
        "carrier": None,
        "total_claims": 0,
        "total_incurred": 0.0,
        "claims_list": [],
    }

    match_insured = re.search(patron_insured, texto)
    if match_insured:
        datos_reporte["insured_name"] = match_insured.group(1).strip()

    match_policy = re.search(patron_policy, texto)
    if match_policy:
        datos_reporte["policy_number"] = match_policy.group(1).strip()

    match_carrier = re.search(patron_carrier, texto)
    if match_carrier:
        datos_reporte["carrier"] = match_carrier.group(1).strip()

    match_claims = re.search(patron_total_claims, texto, re.IGNORECASE)
    if match_claims:
        datos_reporte["total_claims"] = int(match_claims.group(1))

    match_incurred = re.search(patron_total_incurred, texto, re.IGNORECASE)
    if match_incurred:
        datos_reporte["total_incurred"] = float(
            match_incurred.group(1).replace(",", "")
        )

    patron_reclamos = r"(WC-\d{4}-\d{3})\s+([A-Za-z\s,.]+?)\s*\"?\s*(\d{2}/\d{2}/\d{4})\"?\s*\"?\s*(\d{2}/\d{2}/\d{4})\"?\s*\"?\s*(OPEN|CLOSED)\"?"

    reclamos_encontrados = re.findall(patron_reclamos, texto)

    for item in reclamos_encontrados:
        claim_dict = {
            "claim_number": item[0],
            "claimant": item[1].strip(),
            "date_of_loss": item[2],
            "report_date": item[3],
            "status": item[4],
        }
        datos_reporte["claims_list"].append(claim_dict)

    return datos_reporte
