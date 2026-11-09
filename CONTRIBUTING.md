# Gemeinsam beitragen

Die Website wird auf Deutsch gepflegt. Eine QMD-Datei enthält YAML-Metadaten und darunter Text in Markdown. Änderungen erfolgen über einen Branch und Pull Request; eine zweite Person prüft Inhalt und Quellen vor dem Merge nach `main`.

## Ein Projekt hinzufügen

1. `templates/project.qmd` nach `projects/mein-projekt.qmd` kopieren. Dateinamen klein, mit Bindestrichen und ohne Leerzeichen wählen.
2. Titel, Kurzbeschreibung, Kategorien, Bild, Alternativtext und Projektstatus ausfüllen. Vorhandene Kategorien bevorzugen: Quartiere, Sanierung, Energieflexibilität, Lebenszyklus, Lehre & Transfer.
3. Bilder unter `assets/projects/` ablegen. Bildquelle, Urheber und Nutzungsrecht dokumentieren. Nur zur Veröffentlichung bestimmte Inhalte einchecken.
4. Ziele, Vorgehen, Ergebnisse und Quellen ergänzen. Erwartete Ergebnisse ausdrücklich als solche benennen. Nicht belegte Angaben weglassen; Abschluss nicht allein aus einer vergangenen Laufzeit ableiten.
5. `quarto preview` ausführen. Die Projektkarte erscheint automatisch auf der Projektübersicht; Navigation nicht manuell erweitern.
6. Vor dem Pull Request `quarto render` und `python scripts/check_site.py` ausführen.

## Kurzbeispiele

`examples/_template.qmd` unter einem neuen Dateinamen ohne führenden Unterstrich kopieren. Fragestellung, Daten, Schritte, Ergebnisse, Grenzen und Quellen ausfüllen. `draft: true` erst nach Prüfung entfernen und den Beitrag in `examples.qmd` verlinken. Bei mehreren Beiträgen kann dort dasselbe Listing-Prinzip wie auf der Projektübersicht verwendet werden.

## Qualität vor Veröffentlichung

Quellen und Aktualität prüfen, Bildrechte dokumentieren und vertrauliche Inhalte vermeiden. Interne Links, Mobilansicht und Lesbarkeit kontrollieren. `_site/`, `.quarto/` und `.local-sources/` bleiben lokal. Keine Secrets oder Zugangsdaten ablegen.

## Späterer grafischer Editor

Das feste Verzeichnis `projects/`, einheitliches YAML und getrennte Medien lassen sich später auf eine CMS-Collection abbilden. `project-status` ist ein Textfeld; `categories` ist eine Liste, `image` ein Pfad ab Website-Wurzel. Der Dateiname dient als stabile Seitenadresse. Ein Editor kann diese Dateien direkt ändern; Datenbank und Backend sind nicht erforderlich.
