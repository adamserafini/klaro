import os
import xml.etree.ElementTree as ET
import pygtrie

NS = '{http://www.tei-c.org/ns/1.0}'
ENTRY = f'{NS}entry'
FORM = f'{NS}form'  # form: the word in the source language
ORTH = f'{NS}orth'  # orthography: how the word is written
CIT = f'{NS}cit'  # cit: container cited quotation (the translations)
QUOTE = f'{NS}quote'  # the translation itself, in target language
PRON = f'{NS}pron'  # pronunciation
USG = f'{NS}usg'  # Usage (normally a "hint")
NUMBER = f'{NS}num'  # Used to indicate plurality
SENSE = f'{NS}sense'  # Contain the translations
GRAMGRP = f'{NS}gramGrp'  # Container for gender and part-of-speech
POS = f'{NS}pos'  # Part-of-speech eg. noun, verb etc.
GENDER = f'{NS}gen'  # Gender, eg. male, female or neutral
MOOD = f'{NS}mood'  # Grammatical mood of verbs (e.g. subjunctive, imperative)
NOTE = f'{NS}note'  # Alternative field for usage

FILE_DEU_ENG = os.path.join(os.path.dirname(__file__), 'deu-eng.tei')
FILE_ENG_DEU = os.path.join(os.path.dirname(__file__), 'eng-deu.tei')



if __name__ == '__main__':
    # Script to assert the 'shape' of the data
    for dict_file in (FILE_ENG_DEU, FILE_DEU_ENG):
        tree = ET.parse(dict_file)
        root = tree.getroot()

        for entry in root.iter(ENTRY):
            forms = entry.findall(FORM)
            gramgrps = entry.findall(GRAMGRP)
            assert len(forms) == 1
            assert len(gramgrps) == 0 or 1

            form = forms[0]
            for child in form:
                assert child.tag in (PRON, ORTH, USG, NUMBER)

            if gramgrps:
                gramgrp = gramgrps[0]
                for child in gramgrp:
                    assert child.tag in (POS, NUMBER, GENDER, MOOD)

            senses = entry.findall(SENSE)
            for sense in [s for s in senses if s.get('level') != '0']:
                for translation in sense:
                    assert translation.tag == CIT
                    for child in translation:
                        assert child.tag in (QUOTE, GRAMGRP, USG, NOTE)

