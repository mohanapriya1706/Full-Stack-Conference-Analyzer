import pymupdf4llm
import pathlib
import re

# Extract PDF to Markdown
md_text = pymupdf4llm.to_markdown("transcript.pdf")

# Save raw markdown
pathlib.Path("transcript-md-v1.md").write_text(md_text, encoding="utf-8")

# Join broken lines
joined_lines_text = re.sub(r'(?<!\n)\n(?!\n)', ' ', md_text)

# Remove empty lines
cleaned_md_text = re.sub(r"\n\s*\n", "\n\n", joined_lines_text)

# Save cleaned version
pathlib.Path("transcript-md-v2.md").write_text(cleaned_md_text, encoding="utf-8")
