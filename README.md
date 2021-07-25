# QTS – Quick Text Stats
QTS (Quick Text Stats) is a command line tool based on nltk that easily extracts basic measures from raw text using language-specific models. The output language depends on the text language (i.e. english for english texts, italian for italian texts).

### Currently supported languages
- Italian
- English

### Currently included features
- Number of sentences and tokens
- Token/sentence ratio
- Number of tyoe words
- Type/Token ratio
- Number of content vs. functional words
- Part-of-Speech distribution (e.g. number of NOUNs, VERBs, etc.)*
- Part-os-Speech/sentence ratio (e.g. number of NOUNs per sentence)*

*using universal tagset

### Usage
<code>$python3 QTS.py -it your_raw_text.txt</code> # Italian
<br><code>$python3 QTS.py -en your_raw_text.txt</code> # English

### Upcoming features
- Extended language support (French, Spanish, Russian)
- Dependency relation distribution (e.g. number of OBJ relations)
- Dependency relation/sentence ratio (e.g. number of OBJ relation per sentence)
- Other tagsets for PoS-tagging (e.g. PennTreebank tagset)
- Readability indexes 
- Number of paragraphs(?) 
- Number of paragraphs(?) 
