# Static Site Generator

A simple static site generator that converts Markdown files to HTML.

## Requirements
- Python 3.12+
- No virtual environment needed

## Setup
1. Clone repository
2. Create directory structure:
```
.
├── content/         # Markdown files
├── static/         # Static assets (CSS, images)
├── src/           # Python source code
└── template.html  # HTML template
```

## Usage
Run site generator and start local server:
```bash
./main.sh  # Starts server at http://localhost:8888
```

Run tests:
```bash
./test.sh
```

## File Structure
- `content/*.md` - Markdown files get converted to HTML
- `static/*` - Files copied directly to public directory
- `template.html` - Base template for all pages
  - Uses `{{ Title }}` and `{{ Content }}` placeholders

## Supported Markdown
- Headers (h1-h6)
- Bold/Italic text
- Code blocks
- Links and Images
- Ordered/Unordered lists
- Blockquotes