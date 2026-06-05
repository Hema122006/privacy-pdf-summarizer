import re
import spacy

nlp = spacy.load("en_core_web_sm")

def detect_pii(text):

    doc = nlp(text)

    entities = []

    # NLP-based entity detection
    for ent in doc.ents:

        if ent.label_ in [
            "PERSON",
            "ORG",
            "GPE",
            "LOC",
            "FAC"
        ]:
            entities.append(ent.text)

    # Email
    entities.extend(
        re.findall(
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            text
        )
    )

    # Phone
    entities.extend(
        re.findall(
            r'\b\d{10}\b',
            text
        )
    )

    # Aadhaar
    entities.extend(
        re.findall(
            r'\b\d{4}\s\d{4}\s\d{4}\b',
            text
        )
    )

    # PAN
    entities.extend(
        re.findall(
            r'\b[A-Z]{5}[0-9]{4}[A-Z]\b',
            text
        )
    )

    return list(set(entities))