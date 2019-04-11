import numpy as np
import pandas as pd
import requests


url = r"https://dndtools.net/spells/complete-scoundrel--60/blockade--897/"
url2 = r"https://dndtools.net/spells/?name=&range=&spell_resistance=&area=&duration=&saving_throw=&casting_time=&school__slug=&sub_school__slug=&descriptors__slug=&verbal_component=1&somatic_component=1&material_component=1&arcane_focus_component=1&divine_focus_component=1&xp_component=1&rulebook__slug=&rulebook__dnd_edition__slug=core-35&rulebook__dnd_edition__slug=dragonlance&rulebook__dnd_edition__slug=eberron-35&rulebook__dnd_edition__slug=forgotten-realms-35&rulebook__dnd_edition__slug=supplementals-35&description=&class_levels__slug=wizard&spellclasslevel__level=1&domain_levels__slug=&_filter=Filter"


def download_file(url):
    file_data = requests.get(url)
    return file_data.content

