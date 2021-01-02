import sys
from jinja2 import Template


if __name__ == "__main__":
    json_file = sys.argv[1]
    output_file = sys.argv[2]
    report_title = sys.argv[3]
    print(f'generate report "{report_title}" from : "{json_file}"')
    with open(json_file, encoding="UTF-8") as r:
        json_report = r.read()
    with open("templates/report_template.html", encoding="UTF-8") as t:
        template = t.read()
    tmp = Template(template)
    rendered = tmp.render(title=report_title, report_json=json_report)
    with open(output_file, "w", encoding="UTF-8") as html:
        html.write(rendered)
    print(f'created : "{output_file}"')
