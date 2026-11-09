# web

## CBD Forschungswebsite

Deutschsprachiger Quarto-Prototyp für Climate-fit Buildings and Districts an der FH Technikum Wien. 21 Projektseiten, automatische Projektkarten mit Suchfeld und Kategorien, Volltextsuche sowie eine Vorlage für Kurzbeispiele. Keine Datenbank, kein CMS und kein Backend erforderlich.

### Lokal starten

Voraussetzung: Quarto (lokal geprüft mit **1.10.19**). Für den Linkcheck zusätzlich Python 3, ohne Zusatzpakete.

```powershell
quarto preview
```

Quarto zeigt die lokale Vorschauadresse an. Für einen vollständigen Build:

```powershell
quarto render
python scripts/check_site.py
```

Die Ausgabe liegt in `_site/` und wird nicht eingecheckt. Der Check prüft interne Links, Bilder und HTML-Anker; externe Websites werden nicht automatisch auf Erreichbarkeit geprüft.

### GitHub Pages

Remote: `https://github.com/cbd-fhtw/cbd-fhtw.git`.
Daraus abgeleitete Standardadresse: **https://cbd-fhtw.github.io/cbd-fhtw/**. Eine eventuell bereits konfigurierte Custom Domain wurde nicht vorausgesetzt. Die Veröffentlichung ist noch nicht ausgeführt.

Einziger Veröffentlichungsweg: **GitHub Actions → Pages-Artefakt → Pages-Deployment**. Kein `gh-pages`-Branch, kein `/docs`-Ordner und kein lokales `quarto publish` erforderlich.

1. Auf GitHub unter **Settings → Pages → Build and deployment → Source** die Option **GitHub Actions** einstellen.
2. Unter **Settings → Actions → General** sicherstellen, dass GitHub-Actions und `quarto-dev/quarto-actions` zugelassen sind. Organisationsrichtlinien müssen die expliziten Job-Berechtigungen `pages: write` und `id-token: write` erlauben. Ein persönlicher Token ist nicht nötig.
3. Falls das Environment `github-pages` Schutzregeln hat, Deployments von `main` zulassen bzw. erforderliche Reviews ausführen.
4. Nach inhaltlicher Prüfung nach `main` pushen. `.github/workflows/publish.yml` rendert mit den offiziellen Quarto-Actions, prüft interne Links und veröffentlicht `_site`. Alternativ den Workflow manuell über **Actions → Run workflow** starten.
5. Die tatsächliche Deployment-Adresse und den Erfolg im Actions-Lauf prüfen. Bei Repository-Umbenennung oder Custom Domain `website.site-url` in `_quarto.yml` und `BASE` in `scripts/check_site.py` aktualisieren.

Technische Referenzen: [Quarto Actions](https://github.com/quarto-dev/quarto-actions), [GitHub Pages mit eigenem Workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

### Inhalte ergänzen

Projektvorlage: `templates/project.qmd` nach `projects/<name>.qmd` kopieren. Metadaten ausfüllen, Bild nach `assets/projects/` legen und Text ergänzen. Die Karte wird automatisch erzeugt. Pflichtfelder:

```yaml
title: Projektname
description: Kurze Beschreibung
categories: [Quartiere]
image: /assets/projects/mein-bild.jpg
image-alt: Aussagekräftiger Alternativtext
project-status: Laufend
```

Kurzbeispiele beginnen mit einer Kopie von `examples/_template.qmd`. Details und Reviewablauf stehen in [CONTRIBUTING.md](CONTRIBUTING.md).

### Struktur

- `_quarto.yml`, `styles.scss`: Aufbau und Gestaltung.
- `index.qmd`, `projects.qmd`, `examples.qmd`, `about.qmd`: Hauptseiten.
- `projects/`: eine QMD-Datei pro Projekt.
- `assets/`: Teamdarstellung, Teamsymbol und aus den Postern extrahierte Abbildungen.
- `templates/`, `examples/_template.qmd`: Beitragsschablonen, nicht öffentlich gerendert.
- `docs/source-audit.md`: nachvollziehbare Auswahl aller 46 Folien.
- `scripts/check_site.py`: Linkprüfung lokal und in CI.

Die einheitlichen Metadaten und getrennten Medien ermöglichen einen späteren grafischen Editor. Nextcloud, Datenkatalog, Benutzerverwaltung, KI-Konvertierung und Serverinfrastruktur sind nicht implementiert.

### Quellenstand und offene Redaktion

Grundlagen sind die bereitgestellte Projektpräsentation, `klimsta.svg` und die fachlichen Entwicklungsfelder der Strategiepräsentation 2025. Die PowerPoint-Originale, Extraktionsdateien und interne Strategieinhalte bleiben in der ignorierten lokalen Arbeitsablage `.local-sources/` und werden nicht veröffentlicht. `assets/klimsta.svg` wird unverändert als englischsprachige Originalquelle bereitgestellt; die Website-Texte sind deutsch.

„KFZBD“ aus dem Auftrag wird anhand der Quellen als KFCBD/CBD bzw. Climate-fit Buildings and Districts interpretiert. Die Schreibweise CFBD wird dort einbezogen, wo zusätzlich der ausgeschriebene CBD-Schwerpunkt genannt ist. SIMPLY POSITIVE erscheint auf zwei Folien und erhält eine gemeinsame Seite. Alliiertenviertel stammt aus der Teamdarstellung.

TODO vor einer offiziellen Veröffentlichung: Projektstatus und Ergebnislinks bestätigen, Bildurheber und Nutzungsrechte vervollständigen, Teamkontakt sowie Impressum-/Datenschutzangaben ergänzen. Wiederholte Förderbanner aus der Postervorlage werden nicht als projektspezifische Fakten übernommen. Abbildungen und Logos sind nicht pauschal unter eine neue Lizenz gestellt.

### Commit vorbereiten

Nach Prüfung der Änderungen:

```powershell
git add README.md CONTRIBUTING.md .gitignore _quarto.yml styles.scss index.qmd projects.qmd examples.qmd about.qmd projects examples templates assets docs scripts .github/workflows/publish.yml
git commit -m "feat: add German CBD research website with 21 project profiles"
```

Es wurde nicht gepusht. Die lokale Quellablage und der Build sind durch `.gitignore` ausgeschlossen.
