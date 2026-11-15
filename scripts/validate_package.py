#!/usr/bin/env python3
"""Offline integrity and packaging checks for Organic Strategy 1.1.
No live integrations, model execution, rankings, or claimed quality certification.
"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    'SKILL.md', 'README.md', 'LICENSE', 'CHANGELOG.md',
    'chatgpt-custom-gpt-instructions.txt',
    'references/discovery-and-positioning.md',
    'references/seo-research-and-technical.md',
    'references/seo-content-templates.md',
    'references/social-strategy-and-repurposing.md',
    'references/measurement-and-attribution.md',
    'references/industry-playbooks.md',
    'references/policy-accuracy-and-source-notes.md',
    'references/output-templates.md',
    'references/local-seo-kerala-playbook.md',
    'references/malayalam-content-quality.md',
    'references/search-to-social-enquiry-engine.md',
    'references/qualified-enquiry-analytics.md',
    'references/competitor-benchmark-and-originality.md',
    'examples/kerala-training-institute.md',
    'examples/kerala-local-search-to-social.md',
    'tests/manual-evaluations.md',
]
problems=[]
for rel in required:
    if not (root / rel).is_file(): problems.append('Missing '+rel)
if (root/'SKILL.md').is_file():
    text=(root/'SKILL.md').read_text(encoding='utf-8')
    if not text.startswith('---\n'): problems.append('No YAML frontmatter')
    head=text.split('---',2)[1] if text.startswith('---\n') else ''
    if not re.search(r'(?m)^name:\s+organic-strategy\s*$',head): problems.append('Wrong name')
    if not re.search(r'(?m)^description:\s+.+',head): problems.append('Missing description')
    for ref in set(re.findall(r'`((?:references|examples|tests)/[\w./-]+\.md)`',text)):
        if not (root/ref).exists(): problems.append('Broken source reference '+ref)
    for concept in ('Local Growth Sprint','Malayalam Search-to-Social','Source of Truth Card','qualified enquiry','Google Business Profile','AI Overviews'):
        if concept.lower() not in text.lower(): problems.append('Missing '+concept)
    if len(text)<12000: problems.append('SKILL.md seems incomplete')
for text_file in root.rglob('*'):
    if text_file.is_file() and text_file.suffix in ('.md','.txt','.py'):
        try: text_file.read_text(encoding='utf-8')
        except Exception as exc: problems.append(f'Non UTF8 {text_file}: {exc}')
if problems:
    print('FAIL:')
    for p in problems: print(' -',p)
    sys.exit(1)
print('PASS: 21 required files, frontmatter, references, modules, UTF-8 and workflow keywords.')
print('File count:',sum(x.is_file() for x in root.rglob('*')))