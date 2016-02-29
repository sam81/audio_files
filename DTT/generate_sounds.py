# -*- coding: utf-8 -*-

import os

languages = ["en-US", "en-GB", "fr-FR", "it-IT"]
for lan in languages:
    if os.path.exists(lan) == False:
        of.mkdir(lan)
    
#"de-DE", "es-ES"
intro = {}
intro["en-US"] = "the numbers"
intro["en-GB"] = "the numbers"
#intro["de-DE"] = "the numbers"
#intro["es-ES"] = "the numbers"
intro["fr-FR"] = "les chiffres"
intro["it-IT"] = "i numeri"

nums = list(range(11))
for language in languages:
    cmd = 'pico2wave -l="{}" -w="{}/_intro.wav" "{}"'.format(language,language, intro[language])
    os.system(cmd)
    cmd = 'sox {}/_intro.wav -c2 {}/intro.wav rate 48000'.format(language,language)
    os.system(cmd)
    os.remove('{}/_intro.wav'.format(language))
    for num in nums:
        cmd = 'pico2wave -l="{}" -w="{}/_{}.wav" "{}"'.format(language,language, num,num)
        os.system(cmd)
        cmd = 'sox {}/_{}.wav -c2 {}/{}.wav rate 48000'.format(language, num, language, num)
        os.system(cmd)
        os.remove('{}/_{}.wav'.format(language, num))
