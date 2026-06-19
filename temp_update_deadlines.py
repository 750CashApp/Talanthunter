from pathlib import Path

files = [Path('job-list.html'), Path('index.html')]
old = '<span class="text-truncate me-3"><i class="fa fa-map-marker-alt text-primary me-2"></i>USA</span>'
new = '<span class="text-truncate me-3 job-deadline" data-min-days="2" data-max-days="6"></span>'
for p in files:
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if count:
        p.write_text(text.replace(old, new), encoding='utf-8')
        print(f'Updated {count} occurrences in {p.name}')
    else:
        print(f'No occurrences found in {p.name}')
