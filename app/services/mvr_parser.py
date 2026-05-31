import re


def text_processing_mvr(raw_text: str) -> dict:
    text = re.sub(r"\s+", " ", raw_text)

    name_pattern = r"Full\s+Name:\s*(.*?)(?=\s*●|\n|$)"
    dob_pattern = r"Date\s+of\s+Birth:\s*([\d/]+)"
    cld_pattern = r"Driver\s+License\s+Number:\s*([A-Za-z0-9-]+)"
    points_pattern = r"Total\s+Points\s+\(3-Year\s+History\):\s*(\d+)"
    issue_date_pattern = r"Original\s+Issue\s+Date:\s*([\d/]+)"
    expiration_date_pattern = r"Expiration\s+Date:\s*([\d/]+)"
    violation_code_pattern = r"Violation\s+Code:\s*([A-Za-z0-9\s-]+?)(?=\s*●|\n|$)"

    name = re.search(name_pattern, text)
    dob = re.search(dob_pattern, text)
    cld = re.search(cld_pattern, text)
    points = re.search(points_pattern, text)
    issue_date = re.search(issue_date_pattern, text)
    expiration_date = re.search(expiration_date_pattern, text)

    raw_violation_codes = re.findall(violation_code_pattern, text)
    violation_codes = [code.strip() for code in raw_violation_codes]

    total_violations = text.count("Violation Date:")

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
        "violation_codes": violation_codes,
    }

    return driver_profile
