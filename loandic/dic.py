from .entry import read_entry, generate_entries


def expand_dic_csv(input_path, output_path):
    """Expand entries in source dictionary.
    """

    with open(input_path, 'r', encoding="utf-8") as f1, \
         open(output_path, 'w', encoding="utf-8") as f2:
        
        for entry in f1:
            entry = entry.strip("\n")
            fields = read_entry(entry)
            entries = generate_entries(**fields)
            for entry_exp in entries:
                f2.write(entry_exp + "\n")
        