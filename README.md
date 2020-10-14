# MooExt &mdash; Moodle Task ZIP Extractor

_MooExt_ can help teachers to correct homeworks stored in Moodle Task.

When You download students solutions, You obtain ZIP in quite a pitoresque format.

_MooExt_ will extract all students solutions, each file named according to the pattern:
`surname_name_originalfilename.extension`.

## Extraction of ZIP files
If students solution contains ZIP files, they will be extracted to the directory with appropriate name.

Example:
* Student solution contains files:
    - net.pkt
    - config.zip

* Extracted files:
    - surname_name_net.pkt
    - surname_name_config_ZIP &rarr; directory containing files from the config.zip

Usage:
```
python mooext.py downloaded.zip
```
