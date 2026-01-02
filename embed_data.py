import csv
import json
from pathlib import Path

CSV_FILE = "data.csv"
TEMPLATE_FILE = "template.html"
OUTPUT_FILE = "index.html"

def main():
    # Read CSV safely
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Convert numeric fields
    int_fields = {
        "total_limited_5star_count",
        "total_standard_5star_count",
        "action_value",
        "metric_value",
        "p1_eidolon","p2_eidolon","p3_eidolon","p4_eidolon",
        "p1_superimp","p2_superimp","p3_superimp","p4_superimp",
    }

    for row in rows:
        for k in int_fields:
            if k in row and row[k] != "":
                row[k] = int(row[k])

    data_json = json.dumps(rows, ensure_ascii=False)

    # Load template
    template = Path(TEMPLATE_FILE).read_text(encoding="utf-8")

    # Inject data
    output = template.replace("/*__DATA__*/", f"const DATA = {data_json};")

    Path(OUTPUT_FILE).write_text(output, encoding="utf-8")
    print(f"Built {OUTPUT_FILE} with {len(rows)} rows")

if __name__ == "__main__":
    main()
