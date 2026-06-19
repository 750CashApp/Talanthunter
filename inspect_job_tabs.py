from pathlib import Path
import re
html = Path('d:/paidcampaign/job-list.html').read_text(encoding='utf-8')
for tab in ['tab-1','tab-2','tab-3']:
    pat = r'<div id="%s" class="tab-pane([\s\S]*?)(?=<div id="tab-|</div>\s*</div>\s*</div>\s*</div>)' % tab
    m = re.search(pat, html)
    print(tab, 'found' if m else 'NO')
    if m:
        seg = m.group(1)
        print(' jobs:', seg.count('class="job-item'))
        print(' ft:', seg.count('<span class="text-truncate me-3"><i class="far fa-clock text-primary me-2"></i>Full Time</span>'))
        print(' pt:', seg.count('<span class="text-truncate me-3"><i class="far fa-clock text-primary me-2"></i>Part Time</span>'))
