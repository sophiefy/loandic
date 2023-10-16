import csv

from .utils import letters_to_halfwidth, letters_to_fullwidth


# unidic-33 format
FIELD_KEYS = ["surface", "left_id", "rigtn_id", "cost",
              "pos1", "pos2", "pos3", "pos4",
              "ctype", "cform", "lform", "lemma", "orth", "pron", "orthbase", "pronBase",
              "wtype", "itype", "iform", "ftype", "fform", "icontype", "fcontype", "type",
              "kana", "kanabase", "form", "formBase", "atype", "acontype", "amodtype",
              "lid", "lemma_id"]


def read_entry(entry):
    """Read a a entry and load it into a dict object.
    """

    fields = {}
    field_values = next(csv.reader([entry]))
    for field_key, field_value in zip(FIELD_KEYS, field_values):
        fields[field_key] = field_value

    return fields


def generate_entry(**fields):
    """Generate an entry on given field values.
    """

    fields = [str(f) for f in fields.values()]
    entry = ",".join(fields)

    return entry

def generate_entries(**fields):
    """Generate entries on given field values.
    """

    surface = fields.get("surface")

    # convert surface to halfwidth 
    surface_haflwidth = letters_to_halfwidth(surface)
    surface_haflwidth_lower = surface_haflwidth.lower()
    surface_haflwidth_upper = surface_haflwidth.upper()
    surface_haflwidth_cap = surface_haflwidth_lower.capitalize()

    # convert surface to fullwidth
    surface_fullwidth = letters_to_fullwidth(surface)
    surface_fullwidth_lower = surface_fullwidth.lower()
    surface_fullwidth_upper = surface_fullwidth.upper()
    surface_fullwidth_cap = surface_fullwidth_lower.capitalize()
    surface_katakana = fields["pron"]

    # generate expanded entries
    fields["surface"] = surface_haflwidth_lower
    entry_halfwidth_lower = generate_entry(**fields)
    fields["surface"] = surface_haflwidth_upper
    entry_halfwidth_upper = generate_entry(**fields)
    fields["surface"] = surface_haflwidth_cap
    entry_halfwidth_cap = generate_entry(**fields)
    fields["surface"] = surface_fullwidth_lower
    entry_fullwidth_lower = generate_entry(**fields)
    fields["surface"] = surface_fullwidth_upper
    entry_fullwidth_upper = generate_entry(**fields)
    fields["surface"] = surface_fullwidth_cap
    entry_fullwidth_cap = generate_entry(**fields)
    fields["surface"] = surface_katakana
    entry_katakana = generate_entry(**fields)

    entries = [entry_halfwidth_lower, entry_halfwidth_upper, entry_halfwidth_cap,
               entry_fullwidth_lower, entry_fullwidth_upper, entry_fullwidth_cap,
               entry_katakana]
    
    return entries

