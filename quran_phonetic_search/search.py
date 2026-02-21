import csv
from pathlib import Path
from typing import List

from rapidfuzz import process, fuzz

CSV_PATH = Path(__file__).parent / "data" / "quran_words.csv"

class QuranSearch:
    CHOICES:dict = None

    def __init__(self):
        if QuranSearch.CHOICES is None:
            QuranSearch.load()



    def query_word(self,word,limit=1) -> List[str]:
        best_matches=process.extract(query=word,choices=QuranSearch.CHOICES.keys(),scorer=fuzz.WRatio, limit=limit)
        return [QuranSearch.CHOICES[match[0]] for match in best_matches]

    @classmethod
    def load(cls):
        cls.CHOICES = {}
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Combine phonetic_word and simple_latin as key
                key = f"{row['phonetic_word'].lower().strip()}|{row['simple_latin'].lower().strip()}"
                cls.CHOICES[key] = row['arabic_word']


if __name__ == '__main__':
    quranSearch = QuranSearch()
    print(quranSearch.query_word('besm',limit=2))   #['بِسْمِ', 'فَتَبَسَّمَ']
    print(quranSearch.query_word('jahanm',limit=2))   #['جَهَنَّمُ', 'جَهَنَّمَ']
    print(quranSearch.query_word('mohamed',limit=5))   #['حَمِيدًا', 'حَمِيدٌ', 'حَمِيدٍ', 'ٱلْمِهَادُ', 'مُّحَمَّدٌ']

