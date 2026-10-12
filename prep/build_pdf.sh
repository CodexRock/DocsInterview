#!/usr/bin/env bash
# Convertit les documents Markdown du dossier prep/ en PDF (format A5, lisible sur téléphone).
set -euo pipefail
cd "$(dirname "$0")"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
mkdir -p pdf
for md in 0*.md; do
  name="${md%.md}"
  pandoc "$md" -f gfm -t html5 --standalone --embed-resources \
    --css pdf_style.css --metadata title="$name" \
    -V pagetitle="$name" -o "pdf/$name.html"
  # retire le titre généré automatiquement par pandoc
  sed -i 's#<header id="title-block-header">.*</header>##; /<header id="title-block-header">/,/<\/header>/d' "pdf/$name.html"
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="pdf/$name.pdf" "file://$PWD/pdf/$name.html" 2>/dev/null
  rm "pdf/$name.html"
done
ls -la pdf
