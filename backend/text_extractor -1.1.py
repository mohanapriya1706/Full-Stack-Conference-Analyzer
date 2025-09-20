import pymupdf4llm
import pathlib
import re
#from langchain.text_splitter import MarkdownTextSplitter

md_text = pymupdf4llm.to_markdown(r"transcript.pdf")

# Write the text to some file in UTF8-encoding
pathlib.Path("transcript-md-v1.md").write_bytes(md_text.encode())


# Pre-processing step 1: Join single lines
# This regex replaces a newline that is NOT followed by another newline with a single space.
# This helps combine sentences that were broken across multiple lines.
joined_lines_text = re.sub(r'(?<!\n)\n(?!\n)', ' ', md_text)

# Pre-processing stepn 2: Remove empty lines
# The regex pattern r"\n\s*\n" matches one or more newlines with any whitespace in between.
cleaned_md_text = re.sub(r"\n\s*\n", "\n\n", joined_lines_text)


# Write the cleaned text to a file for verification
pathlib.Path("transcript-md-v2.md").write_bytes(cleaned_md_text.encode())

